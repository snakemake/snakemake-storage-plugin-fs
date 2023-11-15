import os
from pathlib import Path
import shutil
import subprocess
from typing import Any, Iterable, Optional

import sysrsync

from snakemake_interface_common.exceptions import WorkflowError
from snakemake_interface_storage_plugins.storage_provider import (
    StorageProviderBase,
    ExampleQuery,
    Operation,
    StorageQueryValidationResult,
)
from snakemake_interface_storage_plugins.storage_object import (
    StorageObjectRead,
    StorageObjectWrite,
    StorageObjectGlob,
)
from snakemake_interface_storage_plugins.io import (
    IOCacheStorageInterface,
    get_constant_prefix,
)


# Required:
# Implementation of your storage provider
# This class can be empty as the one below.
# You can however use it to store global information or maintain e.g. a connection
# pool.
class StorageProvider(StorageProviderBase):
    # For compatibility with future changes, you should not overwrite the __init__
    # method. Instead, use __post_init__ to set additional attributes and initialize
    # futher stuff.

    def __post_init__(self):
        # This is optional and can be removed if not needed.
        # Alternatively, you can e.g. prepare a connection to your storage backend here.
        # and set additional attributes.
        pass

    @classmethod
    def example_query(cls) -> ExampleQuery:
        """Return an example query with description for this storage provider."""
        return ExampleQuery(
            query="test/test.txt",
            description="Some file or directory path.",
        )

    def rate_limiter_key(self, query: str, operation: Operation) -> Any:
        """Return a key for identifying a rate limiter given a query and an operation.

        This is used to identify a rate limiter for the query.
        E.g. for a storage provider like http that would be the host name.
        For s3 it might be just the endpoint URL.
        """
        ...

    def default_max_requests_per_second(self) -> float:
        """Return the default maximum number of requests per second for this storage
        provider."""
        ...

    def use_rate_limiter(self) -> bool:
        """Return False if no rate limiting is needed for this provider."""
        return False

    @classmethod
    def is_valid_query(cls, query: str) -> StorageQueryValidationResult:
        """Return whether the given query is valid for this storage provider."""
        # Ensure that also queries containing wildcards (e.g. {sample}) are accepted
        # and considered valid. The wildcards will be resolved before the storage
        # object is actually used.
        try:
            Path(query)
        except Exception:
            return False

    def list_objects(self, query: Any) -> Iterable[str]:
        """Return an iterator over all objects in the storage that match the query.

        This is optional and can raise a NotImplementedError() instead.
        """
        query = Path(query)
        if query.is_dir():
            return map(str, Path(query).rglob("*"))
        elif query.exists():
            return (query,)
        else:
            return ()


# Required:
# Implementation of storage object. If certain methods cannot be supported by your
# storage (e.g. because it is read-only see
# snakemake-storage-http for comparison), remove the corresponding base classes
# from the list of inherited items.
class StorageObject(StorageObjectRead, StorageObjectWrite, StorageObjectGlob):
    # For compatibility with future changes, you should not overwrite the __init__
    # method. Instead, use __post_init__ to set additional attributes and initialize
    # futher stuff.

    def __post_init__(self):
        # This is optional and can be removed if not needed.
        # Alternatively, you can e.g. prepare a connection to your storage backend here.
        # and set additional attributes.
        self.query_path = Path(self.query)

    async def inventory(self, cache: IOCacheStorageInterface):
        """From this file, try to find as much existence and modification date
        information as possible. Only retrieve that information that comes for free
        given the current object.
        """
        # This is optional and can be left as is

        # If this is implemented in a storage object, results have to be stored in
        # the given IOCache object.
        key = self.cache_key()

        if key in cache.exists_in_storage:
            # already inventorized, stop here
            return

        try:
            stat = self._stat()
        except FileNotFoundError:
            cache.exists_in_storage[key] = False
        if self.query_path.is_symlink():
            # get symlink stat
            lstat = self._stat(follow_symlinks=False)
        else:
            lstat = stat
        cache.mtime[key] = lstat.st_mtime
        cache.size[key] = stat.st_size
        cache.exists_in_storage[key] = True

    def get_inventory_parent(self) -> Optional[str]:
        """Return the parent directory of this object."""
        # this is optional and can be left as is
        parent = self.query_path.parent
        if parent == Path("."):
            return None
        else:
            return parent

    def local_suffix(self) -> str:
        """Return a unique suffix for the local path, determined from self.query."""
        suffix = self.query
        if suffix.startswith("/"):
            # convert absolute path to unique relative path
            suffix = f"__abspath__/{suffix[1:]}"
        return self.query.removeprefix("/")

    def cleanup(self):
        # Nothing to be done here.
        pass

    # Fallible methods should implement some retry logic.
    # The easiest way to do this (but not the only one) is to use the retry_decorator
    # provided by snakemake-interface-storage-plugins.
    def exists(self) -> bool:
        # return True if the object exists
        return self.query_path.exists()

    def mtime(self) -> float:
        # return the modification time
        return self._stat(follow_symlinks=False).st_mtime

    def size(self) -> int:
        # return the size in bytes
        return self._stat().st_size

    def retrieve_object(self):
        # Ensure that the object is accessible locally under self.local_path()
        cmd = sysrsync.get_rsync_command(
            str(self.query_path), str(self.local_path()), options=["-av"]
        )
        self._run_cmd(cmd)

    def store_object(self):
        # Ensure that the object is stored at the location specified by
        # self.local_path().
        cmd = sysrsync.get_rsync_command(
            str(self.local_path()), str(self.query_path), options=["-av"]
        )
        self._run_cmd(cmd)

    def _run_cmd(self, cmd: list[str]):
        try:
            subprocess.run(
                cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
        except subprocess.CalledProcessError as e:
            raise WorkflowError(e.stdout.decode())

    def remove(self):
        # Remove the object from the storage.
        if self.query_path.is_dir():
            shutil.rmtree(self.query_path)
        else:
            self.query_path.unlink()

    def list_candidate_matches(self) -> Iterable[str]:
        """Return a list of candidate matches in the storage for the query."""
        # This is used by glob_wildcards() to find matches for wildcards in the query.
        # The method has to return concretized queries without any remaining wildcards.
        prefix = Path(get_constant_prefix(self.query))
        if prefix.is_dir():
            return map(str, prefix.rglob("*"))
        else:
            return (prefix,)

    def _stat(self, follow_symlinks: bool = True):
        # We don't want the cached variant (Path.stat), as we cache ourselves in
        # inventory and afterwards the information may change.
        return os.stat(self.query_path, follow_symlinks=follow_symlinks)
