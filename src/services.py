from abc import ABC, abstractmethod


class AbstractNLPService(ABC):

    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def ocr_preprocess(self):
        ...

    @abstractmethod
    def tokenizer(self, line: str):
        ...

    @abstractmethod
    def chunker(self):
        ...

    @abstractmethod
    def post_process(self):
        ...


class AGCSNLPService(AbstractNLPService):

    def __init__(self, config: dict):
        super().__init__(config)

    def ocr_preprocess(self):
        pass

    def tokenizer(self, line: str):
        pass

    def chunker(self):
        pass

    def post_process(self):
        pass


class AGINLPService(AbstractNLPService):

    def ocr_preprocess(self):
        pass

    def tokenizer(self, line: str):
        pass

    def chunker(self):
        pass

    def post_process(self):
        pass

    @abstractmethod
    def finance_risk(self):
        ...


class AGIBankNLPService(AGINLPService):
    def finance_risk(self):
        pass


class AGIRealEstateNLPService(AGINLPService):
    def finance_risk(self):
        pass
