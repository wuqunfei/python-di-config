from abc import ABC, abstractmethod
from loguru import logger

from src.gateway import DatabaseGateway, ObjectStorageGateway


class AbstractNLPService(ABC):

    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def ocr_preprocess(self):
        ...

    @abstractmethod
    def tokenizer(self):
        ...

    @abstractmethod
    def chunker(self):
        ...

    @abstractmethod
    def post_process(self):
        ...

    def run_nlp(self):
        self.ocr_preprocess()
        self.tokenizer()
        self.chunker()
        self.post_process()


class BankNLPService(AbstractNLPService):

    def __init__(self,
                 config: dict,
                 db_gateway: DatabaseGateway,
                 storage_gateway: ObjectStorageGateway):
        super().__init__(config)

        self.db_gateway = db_gateway
        self.storage_gateway = storage_gateway

    def ocr_preprocess(self):
        self.storage_gateway.download()
        logger.info(f"{self.__class__.__name__} OCR preprocess done")

    def tokenizer(self):
        logger.info(f"{self.__class__.__name__} Tokenizer done")

    def chunker(self):
        logger.info(f"{self.__class__.__name__} Chunker done")

    def post_process(self):
        logger.info(f"{self.__class__.__name__} post process done")
        logger.info(self.config)
        self.db_gateway.save()


class InsuranceNLPService(AbstractNLPService):

    def __init__(self, config: dict):
        super().__init__(config)

    def ocr_preprocess(self):
        logger.info(f"{self.__class__.__name__} OCR preprocess done")

    def tokenizer(self):
        logger.info(f"{self.__class__.__name__} Tokenizer done")

    def chunker(self):
        logger.info(f"{self.__class__.__name__} Chunker done")

    def post_process(self):
        logger.info(f"{self.__class__.__name__} post process done")

    @abstractmethod
    def get_risk(self):
        ...


class LifeNLPService(InsuranceNLPService):
    def get_risk(self):
        logger.info(f"{self.__class__.__name__} risk score 1.0 done")


class CarNLPService(InsuranceNLPService):
    def get_risk(self):
        logger.info(f"{self.__class__.__name__} risk score 2.0 done")
