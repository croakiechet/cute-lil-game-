import pygame
import json


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace('png', 'json')
        self.screensize = pygame.display.get_surface().get_size()
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name, scale):
        sprite = self.data['frames'][name]['frame']
        self.x, self.y, self.w, self.h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(self.x, self.y, self.w, self.h)
        self.new_w, self.new_h = self.w * scale, self.h * scale
        image = pygame.transform.scale(image, (self.new_w, self.new_h))
        return image
