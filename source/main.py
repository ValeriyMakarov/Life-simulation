import sys
import configparser
import os
import pygame
import logging
import re

ROOT = re.sub('(.*Life-simulation).*', r'\1', os.getcwd())
CONFIG_PATH: str = os.path.join(ROOT, 'config.ini')

log = logging.getLogger()


def initialize_settings() -> None:
    config = configparser.ConfigParser()

    if not config.read(CONFIG_PATH):
        config['logger'] = {
            'level': 'DEBUG',
            'log_folder': 'logs'
        }
        with open(CONFIG_PATH, 'w') as file:
            config.write(file)

    logging.basicConfig(
        level=logging.getLevelName(config['logger']['level'].upper()),
        datefmt='%y/%m/%d %H:%M:%S',
        style='{',
        format='[{asctime} {levelname}] : {module}.{funcName}\n\t{message}',
        stream=sys.stdout
    )


def loop() -> None:
    log.info('Starting game.')
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
    log.info('Game stopped.')


if __name__ == '__main__':
    initialize_settings()
    loop()
