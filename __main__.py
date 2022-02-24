from dependency_injector import providers
from pydantic import validator
from pydantic.dataclasses import dataclass
import hydra
from hydra.core.config_store import ConfigStore
from src.containers import MyContainer
from src.services import ExtraDynamicService


@dataclass
class MySQLConfig:
    driver: str
    user: str
    port: int
    password: str

    @validator('port', pre=True)
    def check_port(cls, port):
        if port < 1024:
            raise Exception(f"Port:{port} < 1024 is forbidden ")
        return port


cs = ConfigStore.instance()
cs.store(name="config", node=MySQLConfig, group='')


@hydra.main(config_path="", config_name="config")
def my_app(cfg: MySQLConfig) -> None:
    """1. to get config yaml by hydra"""
    cfg_dict = dict(cfg)
    """2. to validate the configuration by pydantic"""
    MySQLConfig(**cfg_dict)
    container = MyContainer()
    """3. to load configuration into container"""
    container.config.from_dict(cfg_dict)

    nlp = container.nlp_service_factory()
    nlp.run_nlp()

    """https://python-dependency-injector.ets-labs.org/containers/dynamic.html"""
    container.extra_service_factory = providers.Factory(ExtraDynamicService)
    extra_service = container.extra_service_factory()
    extra_service.echo()


if __name__ == "__main__":
    my_app()
