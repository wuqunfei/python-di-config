from typing import Union

from pydantic import validator
from pydantic.dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore

from src.containers import MyContainer


@dataclass
class MySQLConfig:
    driver: str
    user: str
    port: int
    password: str

    # @validator('port', pre=True)
    # def check_port(cls, v):
    #     if v > 3306:
    #         raise Exception(f"Port is wrong {v}")
    #     return v
    #
    # @validator('password', pre=True)
    # def check_pwd(cls, v):
    #     if not v or len(v) < 6:
    #         raise Exception('f"pwd is too short"')


cs = ConfigStore.instance()
cs.store(name="config", node=MySQLConfig, group='.')


@hydra.main(config_path="", config_name="config")
def my_app(cfg: MySQLConfig) -> None:
    cfg_dict = dict(cfg)
    '''to validate the configuration by pydantic'''
    configuration = MySQLConfig(**cfg_dict)

    '''to load configuration from dict'''
    container = MyContainer()
    container.config.from_dict(cfg_dict)


if __name__ == "__main__":
    my_app()
