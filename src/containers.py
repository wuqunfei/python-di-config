from dependency_injector import containers, providers

from src.services import MysqlGateWay, S3GateWay


class MyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    mysql_gateway = providers.Singleton(
        MysqlGateWay
    )
    s3_gateway = providers.Singleton(
        S3GateWay
    )
