import pygame


class Engine:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, scene):
        self.running = True
        self.scene = scene
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        pygame.init()

    def run(self):
        while self.running:
            ...
            self.clock.tick(60)

        pygame.quit()
