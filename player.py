import pygame
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.load_frames()
        self.x = x
        self.y = y
        self.current_image = self.idle_frames_left[0]
        self.rect = self.current_image.get_rect()
        self.current_frame = 0
        self.last_updated = 0
        self.walk_speed = 3
        self.state = 'idle'
        self.scale = scale
        self.facing_left = False
        self.now = pygame.time.get_ticks()
        self.image_size = self.current_image.get_size()

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    def animate(self):
        self.now = pygame.time.get_ticks()
        match self.state:
            case 'idling':
                self.idle()
            case 'walking':
                self.walk()
            case 'jumping':
                pass
            case 'landing':
                pass
            case 'sneaking':
                pass

    def idle(self):
        if self.now - self.last_updated > 150:
            self.last_updated = self.now
            self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
            if self.facing_left:
                self.current_image = self.idle_frames_left[self.current_frame]
            else:
                self.current_image = self.idle_frames_right[self.current_frame]

    def walk(self):
        if self.now - self.last_updated > 90:
            self.last_updated = self.now
            self.current_frame = (self.current_frame + 1) % len(self.walk_frames_left)
            if self.facing_left:
                self.current_image = self.walk_frames_left[self.current_frame]
            else:
                self.current_image = self.walk_frames_right[self.current_frame]

    def idle(self):
        if self.now - self.last_updated > 150:
            self.last_updated = self.now
            self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
            if self.facing_left:
                self.current_image = self.idle_frames_left[self.current_frame]
            else:
                self.current_image = self.idle_frames_right[self.current_frame]

    def load_frames(self):
        my_spritesheet = Spritesheet('sprites/spritesheet.png')

        # idle
        self.idle_frames_right = []
        for frame in range(7):
            self.idle_frames_right.append(my_spritesheet.parse_sprite(('idle' + str(frame) + ".png"), self.scale))

        self.idle_frames_left = []
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))

        # walk
        self.walk_frames_right = []
        for frame in range(7):
            self.walk_frames_right.append(my_spritesheet.parse_sprite(('walk' + str(frame) + ".png"), self.scale))

        self.walk_frames_left = []
        for frame in self.walk_frames_right:
            self.walk_frames_left.append(pygame.transform.flip(frame, True, False))

        # jump
        self.jump_frames_right = []
        for frame in range(3):
            self.jump_frames_right.append(my_spritesheet.parse_sprite(('jump' + str(frame) + ".png"), self.scale))

        self.jump_frames_left = []
        for frame in self.jump_frames_right:
            self.jump_frames_left.append(pygame.transform.flip(frame, True, False))

        # land
        self.land_frames_right = []
        for frame in range(2):
            self.land_frames_right.append(my_spritesheet.parse_sprite(('land' + str(frame) + ".png"), self.scale))

        self.land_frames_left = []
        for frame in self.land_frames_right:
            self.land_frames_left.append(pygame.transform.flip(frame, True, False))

        # sneak
        self.sneak_frames_right = []
        for frame in range(7):
            self.sneak_frames_right.append(my_spritesheet.parse_sprite(('sneak' + str(frame) + ".png"), self.scale))
        self.sneak_frames_left = []
        for frame in self.sneak_frames_right:
            self.sneak_frames_left.append(pygame.transform.flip(frame, False, True))






