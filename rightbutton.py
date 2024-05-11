import pygame


class RightButton(pygame.sprite.Sprite):
    def __init__(self, scale):
        super().__init__()
        self.image = pygame.image.load("sprites/Right.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * scale, self.image.get_height() * scale))
        self.image_size = self.image.get_size()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def get_img_size(self):
        return self.image_size
