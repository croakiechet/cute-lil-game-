import pygame


class CatFrame:
    def __init__(self, scale, screensize):
        self.image = pygame.image.load("sprites/catframe.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.screensize = screensize

    def set_position(self):
        catframe_width, catframe_height = self.rect.size
        x_centered = (self.screensize[0] / 2) - (catframe_width / 2)
        y_centered = (self.screensize[1] / 2) - (catframe_height / 2)
        self.rect.topleft = (x_centered, y_centered)
        return self.rect.topleft
