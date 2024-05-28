import pygame


class SpriteSheet:
    def __init__(self, screen, filename):
        self.filename = filename
        self.spritesheet = pygame.image.load(filename).convert()
        self.screensize = screen


    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.spritesheet, (0,0), (x, y, w, h))
        return sprite

