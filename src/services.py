from abc import ABC, abstractmethod
from loguru import logger


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


class AGCSNLPService(AbstractNLPService):

    def __init__(self, config: dict):
        super().__init__(config)

    def ocr_preprocess(self):
        logger.info("AGCS OCR preprocess done")

    def tokenizer(self):
        logger.info("AGCS Tokenizer  done")

    def chunker(self):
        logger.info("AGCS Chunker done")

    def post_process(self):
        logger.info("AGCS post process done")
        logger.info(self.config)


class AGINLPService(AbstractNLPService):

    def ocr_preprocess(self):
        logger.info("AGI OCR preprocess done")

    def tokenizer(self):
        logger.info("AGI Tokenizer done")

    def chunker(self):
        logger.info("AGI Chunker done")

    def post_process(self):
        logger.info("AGI post process done")

    @abstractmethod
    def finance_risk(self):
        ...


class AGIBankNLPService(AGINLPService):
    def finance_risk(self):
        logger.info("AGI Bank RISK process done")


class AGIRealEstateNLPService(AGINLPService):
    def finance_risk(self):
        logger.info("AGI Real Estate process done")
