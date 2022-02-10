from dependency_injector import containers, providers

from src.gateway import MysqlGateway, S3GateWay, ObjectStorageGateway, DatabaseGateway
from src.services import AbstractNLPService, BankNLPService


class MyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    '''Gateway Factory'''
    mysql_gateway: DatabaseGateway = providers.Singleton(
        MysqlGateway
    )
    s3_gateway: ObjectStorageGateway = providers.Singleton(
        S3GateWay
    )

    '''Services '''
    nlp_service_factory: AbstractNLPService = providers.Factory(
        BankNLPService,
        config=config,
        db_gateway=mysql_gateway
    )
