from dependency_injector import containers, providers

from src.gateway import MysqlGateWay, S3GateWay
from src.services import AGCSNLPService, AbstractNLPService


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
    agcs_nlp_service: AbstractNLPService = providers.Factory(
        AGCSNLPService
    )
