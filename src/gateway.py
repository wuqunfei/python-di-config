from abc import ABC, abstractmethod
from loguru import logger


class DatabaseGateway(ABC):

    def __init__(self):
        ...

    @abstractmethod
    def save(self):
        ...


class MysqlGateway(DatabaseGateway):
    def __init__(self):
        ...

    def save(self):
        logger.info("Saved in Mysql")


class PostgresqlGateway(DatabaseGateway):
    def __init__(self):
        ...

    def save(self):
        logger.info("Saved in Postgresql")


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
