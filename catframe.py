import pygame


class CatFrame:
    def __init__(self, image):
        self.sheet = image

    def return_image(self, width, height, scale):
        image = pygame.Surface([width, height], pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (width*scale, height*scale))
        image = pygame.transform.scale(self.sheet, (width * scale, height * scale))

        return image
