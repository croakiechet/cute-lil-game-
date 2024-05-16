import pygame


class HeadSheet:
    def __init__(self, screensize):
        self.image = pygame.image.load("sprites/headsheet.png")
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.screensize = screensize
        self.pygam

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def set_position(self):
        sprite_width, sprite_height = self.rect.size
        x_centered = (self.screensize[0] / 2) - (sprite_width / 2)
        y_centered = (self.screensize[1] / 2) - (sprite_height / 2)
        self.rect.topleft = (x_centered, y_centered)
        return self.rect.topleft