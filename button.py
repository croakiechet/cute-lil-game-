import pygame


class Button:
    def __init__(self, image, scale, screensize):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() * scale, self.image.get_height() * scale)
        )
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.screen_size = screensize
        self.mask = pygame.mask.from_surface(self.image)

    def set_position(self):
        button_width, button_height = self.rect.size
        x_centered = (self.screen_size[0] / 2) - (button_width / 2)
        y_centered = (self.screen_size[1] / 2) - (button_height / 2)
        return x_centered, y_centered

    def rect_maker(self, x, y):
        self.rect = pygame.Rect(x, y, self.rect.size[0], self.rect.size[1])
