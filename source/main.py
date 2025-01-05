import logging
# import random
# import pygame

from core.init_utils import LoggerInitializer, ConfigInitializer
from core.engine import Engine

log: logging.Logger

# class BackgroundGroup(pygame.sprite.Group):
#     def __init__(self):
#         super().__init__()
#         self.display_surface=pygame.display.get_surface()
#         self.offset = pygame.Vector2()
#
#     def draw(self, offset):
#
#         self.offset.x = offset[0]
#         self.offset.y = offset[1]
#         for i in self.sprites():
#
#             self.display_surface.blit(
#                 i.image,
#                 i.rect.topleft+self.offset)
#
#
# class BackgroundElement(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface([10, 10])
#         self.image.fill((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.k_zoom = 1




# def loop() -> None:
#     log.info('Starting game.')
#     pygame.init()
#     screen = pygame.display.set_mode((1280, 720))
#     clock = pygame.time.Clock()
#     running = True
#
#     background = BackgroundGroup()
#     for i in range(250):
#         for j in range(250):
#             x=i*10
#             y=j*10
#             n=BackgroundElement(x,y)
#             background.add(n)
#
#     dragging = False
#     offset = (0,0)
#     zoom = 0
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 log.debug('QUIT action initialized.')
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 log.debug('Mouse button pressed.')
#                 dragging = True
#             elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#                 log.debug('Mouse button unpressed.')
#                 dragging = False
#             if event.type == pygame.MOUSEMOTION and dragging:
#                 log.debug(f'Mouse motion.')
#                 rel = event.rel
#                 offset = (offset[0] + rel[0], offset[1] + rel[1])
#                 log.debug(f'{offset=}')
#             if event.type == pygame.MOUSEWHEEL:
#                 zoom += event.y
#                 log.debug(f'{zoom=}')
#
#         screen.fill('white')
#         background.draw(offset)
#         pygame.display.flip()
#
#         clock.tick(60)
#     pygame.quit()
#     log.info('Game stopped.')

# scene = pygame.rect.Rect((0,0),)


if __name__ == '__main__':
    ConfigInitializer.init()
    LoggerInitializer.init(
        ConfigInitializer.config.get('logger', 'level', fallback='INFO')
    )
    log = LoggerInitializer.log
    engine = Engine()
