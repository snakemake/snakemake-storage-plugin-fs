from typing import Optional, Type
import uuid
from snakemake_interface_storage_plugins.tests import TestStorageBase
from snakemake_interface_storage_plugins.storage_provider import StorageProviderBase
from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase
from snakemake_storage_plugin_fs import StorageProvider


class TestStorageNoSettings(TestStorageBase):
    __test__ = True
    retrieve_only = False

    def get_query(self) -> str:
        return "test/test.txt"

    def get_query_not_existing(self) -> str:
        return f"test/{uuid.uuid4().hex}"

    def get_storage_provider_cls(self) -> Type[StorageProviderBase]:
        return StorageProvider

    def get_storage_provider_settings(self) -> Optional[StorageProviderSettingsBase]:
        return None
