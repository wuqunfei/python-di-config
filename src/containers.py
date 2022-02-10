from dependency_injector import containers, providers

from src.gateway import MysqlGateway, S3GateWay, ObjectStorageGateway, DatabaseGateway
from src.services import AbstractNLPService, BankNLPService, LifeNLPService, CarNLPService


class MyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    '''Gateways'''
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
        db_gateway=mysql_gateway,
        storage_gateway=s3_gateway

    )

    life_nlp_factory: AbstractNLPService = providers.Factory(
        LifeNLPService,
        config=config
    )

    car_nlp_factory: AbstractNLPService = providers.Factory(
        CarNLPService,
        config=config
    )
