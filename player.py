import pygame
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, scale):
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = pygame.display.get_surface().get_size()
        self.x = x
        self.current_frame = 0
        self.last_updated = pygame.time.get_ticks()
        self.walk_speed = 2
        self.jump_speed = 0
        self.sneak_speed = 0
        self.state = 'idle'
        self.scale = scale
        self.facing_left = False
        self.now = pygame.time.get_ticks()
        self.load_frames()
        self.current_image = self.idle_frames_left[0]
        self.rect = self.current_image.get_rect()
        self.image_size = self.current_image.get_size()
        self.y = self.screen_size[1] - (self.image_size[1] - 63)
        self.time_of_last_jump = 0
        self.time_of_jump_deactivate = 0
        self.time_since_last_jump = 0
        self.time_since_jump_activated = 0

    def move(self):
        if self.state == 'walking':
            if self.facing_left:
                self.x -= self.walk_speed
            if not self.facing_left:
                self.x += self.walk_speed
        if self.state == 'sneaking':
            if self.facing_left:
                self.x -= self.sneak_speed
            if not self.facing_left:
                self.x += self.sneak_speed
        if self.state == 'jumping':
            if self.facing_left:
                self.x -= self.jump_speed
            if not self.facing_left:
                self.x += self.jump_speed

    def draw(self, screen):
        # move character, then blit
        screen.blit(self.current_image, (self.x, self.y))

    def animate(self):
        self.now = pygame.time.get_ticks()
        match self.state:
            case 'idling':
                self.action('idle', 150)
            case 'walking':
                self.action('walk', 100)
            case 'jumping':
                self.action('jump', 150)
            case 'landing':
                self.action('land', 150)
            case 'sneaking':
                self.action('sneak', 150)
            case 'blinking':
                self.action('idleblink', 150)
            case 'attacking':
                self.action('attack', 150)

    def action(self, action: str, time_between_frames: int):
        if self.now - self.last_updated > time_between_frames:
            self.last_updated = self.now
            if self.facing_left:
                facing = "left"
            else:
                facing = "right"

            action_frames = getattr(self, f'{action}_frames_{facing}') # getting self.(WHATEVER FRAMES I WANT)
            self.current_frame = (self.current_frame + 1) % len(action_frames)
            self.current_image = action_frames[self.current_frame]

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
            self.sneak_frames_left.append(pygame.transform.flip(frame, True, False))

        # idle blink
        self.idleblink_frames_right = []
        for frame in range(7):
            self.idleblink_frames_right.append(my_spritesheet.parse_sprite(('idleblink' + str(frame) + ".png"), self.scale))
        self.idleblink_frames_left = []
        for frame in self.sneak_frames_right:
            self.idleblink_frames_left.append(pygame.transform.flip(frame, True, False))

        # attack
        self.attack_frames_right = []
        for frame in range(6):
            self.attack_frames_right.append(my_spritesheet.parse_sprite(('attack' + str(frame) + ".png"), self.scale))
        self.attack_frames_left = []
        for frame in self.sneak_frames_right:
            self.attack_frames_left.append(pygame.transform.flip(frame, True, False))
