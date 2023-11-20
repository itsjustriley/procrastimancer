import pygame 
from random import randint, choice
from constants import screen, left_top_bound, right_bottom_bound, frame_rate, lanes, sprite_width

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        if isinstance(image, str):
            self.surf = pygame.image.load(image)
            self.animated = False
        else:
            self.animated = True
            self.animations = image
            if "idle" in self.animations:
                self.state = "idle"
            elif "run_right" in self.animations:
                self.state = "run_right"
            else:
                self.state = "tea"
            self.frame = 0
            self.surf = self.animations[self.state][self.frame]
            self.frame_delay = frame_rate
            self.facing = "right"
            self.revive_complete = False
        self.rect = self.surf.get_rect()
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()
        self.respawned = False
 
    def render(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.animated:
            self.frame_delay -= 1
            if self.frame_delay <= 0:
                self.surf = self.get_next_frame()
                self.frame_delay = frame_rate
        screen.blit(self.surf, (self.x, self.y))

    def set_speed(self, num):
        return ((randint(0, 200) / 100) + 1) + (num / 5)
    
    def reset(self):
        v_or_h = choice(['v', 'h'])
        lane = choice(lanes)
        speed_choice = choice([self.speed, -self.speed])
        if v_or_h == 'v':
            self.x = lane
            self.dy = speed_choice
            self.dx = 0
            self.y = -64 if self.dy > 0 else right_bottom_bound
            self.state = "run_up" if self.dy > 0 else "run_down"
        else:
            self.y = lane
            self.dx = speed_choice
            self.dy = 0
            self.x = -64 if self.dx > 0 else right_bottom_bound
            self.facing = "left" if self.dx < 0 else "right"

    def move(self): 
        self.x += self.dx
        self.y += self.dy
        if self.x > right_bottom_bound+sprite_width:
            self.reset()
        if self.x < left_top_bound-sprite_width:
            self.reset()
        if self.y > right_bottom_bound+sprite_width:
            self.reset()
        if self.y < left_top_bound-sprite_width:
            self.reset()

    def get_next_frame(self):
        self.frame += 1
        if self.frame >= len(self.animations[self.state]):
            if self.state == "revive":
                self.state = "idle"
                self.controlled = True
                self.respawned = True
            elif self.state == "death":
                self.frame = len(self.animations[self.state]) - 1
                if self.facing == "left":
                    return pygame.transform.flip(self.animations[self.state][self.frame], True, False).convert_alpha()
                return self.animations[self.state][self.frame]
            self.frame = 0
            if "idle" in self.animations:
                self.state = "idle"
        if self.facing == "left":
            return pygame.transform.flip(self.animations[self.state][self.frame], True, False).convert_alpha()
        return self.animations[self.state][self.frame]


    





