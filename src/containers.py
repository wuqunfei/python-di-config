from dependency_injector import containers, providers

from src.gateway import MysqlGateWay, S3GateWay
from src.services import AbstractNLPService, BankNLPService


class MyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    '''Gateway Factory'''
    mysql_gateway = providers.Singleton(
        MysqlGateWay
    )
    s3_gateway = providers.Singleton(
        S3GateWay
    )

    '''Services '''
    nlp_service_factory: AbstractNLPService = providers.Factory(
        BankNLPService,
        config=config,
        db_gateway=mysql_gateway
    )
