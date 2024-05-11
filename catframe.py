import pygame


class CatFrame:
    def __init__(self, scale):
        self.image = pygame.image.load("sprites/catframe.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def get_img_size(self):
        return self.image_size
