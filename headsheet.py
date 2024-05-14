import pygame


class HeadSheet:
    def __init__(self):
        self.image = pygame.image.load("sprites/headsheet.png")
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect()

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

