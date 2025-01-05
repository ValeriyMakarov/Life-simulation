import pygame

from source.core.init_utils import LoggerInitializer

log = LoggerInitializer.log


class Engine:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        pygame.init()

    def run(self) -> None:
        log.debug(self.running)
        while self.running:
            log.debug("run")
            ...
            self.clock.tick(60)

        pygame.quit()

    def scene_size(self) -> tuple:
        return self.screen.get_size()