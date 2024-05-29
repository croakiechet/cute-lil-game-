import pygame
from spritesheet import Spritesheet

class Player:
    def __init__(self, x, y, scale):
        my_spritesheet = Spritesheet('spritesheet.png')
        self.x = x
        self.y = y
        self.image_original = my_spritesheet.parse_sprite("idle1.png")
        self.image = pygame.transform.scale(self.image_original, scale)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3
        self.current_direction = "right"
        self.scale = scale
        self.screen = pygame.display.get_window_size()

    def set_position(self):
        sprite_width, sprite_height = self.rect.size
        x_centered = (self.screen[0] / 2) - (sprite_width / 2)
        y_centered = (self.screen[1] / 2) - (sprite_height / 2)
        self.rect.topleft = (x_centered, y_centered)
        return self.rect.topleft

    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        if direction == "right":
            self.current_direction = "right"
            self.x += self.delta
        if direction == "left":
            self.current_direction = "left"
            self.x -= self.delta
