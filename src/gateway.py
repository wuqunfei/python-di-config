from abc import ABC, abstractmethod
from loguru import logger


class MysqlGateWay:
    def __init__(self):
        ...


class ObjectStorageGateway(ABC):

    def __init__(self):
        ...

    @abstractmethod
    def download(self):
        ...


class S3GateWay(ObjectStorageGateway):
    def download(self):
        logger.info("download from AWS S3 blob Storage")


class AzureStoreGateWay(ObjectStorageGateway):
    def download(self):
        logger.info("download from Azure Object Storage")
