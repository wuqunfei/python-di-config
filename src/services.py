from abc import ABC, abstractmethod
from loguru import logger

from src.gateway import MysqlGateWay


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
                 db_gateway: MysqlGateWay):
        super().__init__(config)

        self.db_gateway = db_gateway

    def ocr_preprocess(self):
        logger.info(f"{self.__class__.__name__} OCR preprocess done")

    def tokenizer(self):
        logger.info(f"{self.__class__.__name__} Tokenizer done")

    def chunker(self):
        logger.info(f"{self.__class__.__name__} Chunker done")

    def post_process(self):
        logger.info(f"{self.__class__.__name__} post process done")
        logger.info(self.config)


class InsuranceNLPService(AbstractNLPService):

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


class AutoNLPService(InsuranceNLPService):
    def get_risk(self):
        logger.info(f"{self.__class__.__name__} risk score 2.0 done")
