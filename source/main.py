import math
import random
import sys
import configparser
import os
import pygame
import logging
import re

ROOT = re.sub('(.*Life-simulation).*', r'\1', os.getcwd())
CONFIG_PATH: str = os.path.join(ROOT, 'config.ini')

log = logging.getLogger()

def get_k_zoom(x):
    # todo при 0 зуме ~ 1. нужно найти другую формулу
    return 10/(1+math.e**(-x+11/5))

class BackgroundGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface=pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, offset, zoom):
        k_zoom = get_k_zoom(zoom)
        self.offset.x = offset[0]
        self.offset.y = offset[1]
        for i in self.sprites():
            if i.k_zoom != k_zoom:
                i.scale(k_zoom)
            self.display_surface.blit(
                i.image,
                i.rect.topleft+self.offset)


class BackgroundElement(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.k_zoom = 1

    def scale(self, k_zoom):
        self.image = pygame.transform.scale(
            self.image,
            (self.rect.width * k_zoom, self.rect.height * k_zoom)
        )
        self.rect = self.image.get_rect()

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

    background = BackgroundGroup()
    for i in range(150):
        for j in range(100):
            x=i*10
            y=j*10
            n=BackgroundElement(x,y)
            background.add(n)
    dragging = False
    offset = (0,0)
    zoom = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log.debug('QUIT action initialized.')
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                log.debug('Mouse button pressed.')
                dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                log.debug('Mouse button unpressed.')
                dragging = False
            if event.type == pygame.MOUSEMOTION and dragging:
                log.debug(f'Mouse motion.')
                rel = event.rel
                offset = (offset[0] + rel[0], offset[1] + rel[1])
                log.debug(f'{offset=}')
            if event.type == pygame.MOUSEWHEEL:
                zoom += event.y
                log.debug(f'{zoom=}')

        screen.fill('white')
        background.draw(offset, zoom)
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
    log.info('Game stopped.')


if __name__ == '__main__':
    initialize_settings()
    loop()
