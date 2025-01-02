import sys
import configparser
import os
import re
import logging


class LoggerInitializer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            logging.basicConfig(
                level=logging.getLevelName(kwargs['level'].upper()),
                datefmt='%y/%m/%d %H:%M:%S',
                style='{',
                format='[{asctime} {levelname}] : {module}.{funcName}\n\t{message}',
                stream=sys.stdout
            )
        return logging.getLogger()


class ConfigInitializer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        config = None
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            # указать вечный корень типа C:/Programs...
            root = re.sub('(.*Life-simulation).*', r'\1', os.getcwd())
            config_path = os.path.join(root, 'config.ini')
            config = configparser.ConfigParser()

            if not config.read(config_path):
                config['logger'] = {
                    'level': 'DEBUG',
                    'log_folder': 'logs'
                }
                with open(config_path, 'w') as file:
                    config.write(file)
        return config
