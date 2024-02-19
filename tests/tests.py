import os
from typing import Optional, Type
import uuid
from snakemake_interface_storage_plugins.tests import TestStorageBase
from snakemake_interface_storage_plugins.storage_provider import StorageProviderBase
from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase
from snakemake_storage_plugin_fs import StorageProvider


class TestStorageNoSettings(TestStorageBase):
    __test__ = True
    retrieve_only = False
    touch = True

    def get_query(self, tmp_path) -> str:
        parent = f"{tmp_path}/storage/test/"
        os.makedirs(parent, exist_ok=True)
        return f"{parent}/test.txt"

    def get_query_not_existing(self, tmp_path) -> str:
        return f"{tmp_path}/storage/test/{uuid.uuid4().hex}"

    def get_storage_provider_cls(self) -> Type[StorageProviderBase]:
        return StorageProvider

    def get_storage_provider_settings(self) -> Optional[StorageProviderSettingsBase]:
        return None
