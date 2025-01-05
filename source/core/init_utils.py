import sys
import configparser
import os
import re
from logging import Logger, getLogger, basicConfig, getLevelName


class LoggerInitializer:
    log: Logger = None

    @classmethod
    def init(cls, level='INFO'):
        basicConfig(
            level=getLevelName(level.upper()),
            datefmt='%y/%m/%d %H:%M:%S',
            style='{',
            format='[{asctime} {levelname}] : {module}.{funcName}\n\t{message}',
            stream=sys.stdout
        )
        cls.log = getLogger()


class ConfigInitializer:
    config: configparser.ConfigParser
    config_path: str

    @classmethod
    def init(cls):
        root = re.sub('(.*Life-simulation).*', r'\1', os.getcwd())
        cls.config_path = os.path.join(root, 'config.ini')
        cls.config = configparser.ConfigParser()
        if not cls.config.read(cls.config_path):
            cls.__create_config()

    @classmethod
    def __create_config(cls):
        cls.config['logger'] = {
            'level': 'DEBUG',
            'log_folder': 'logs'
        }
        with open(cls.config_path, 'w') as file:
            cls.config.write(file)
