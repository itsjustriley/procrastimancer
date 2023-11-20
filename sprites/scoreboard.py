from typing import Any
import pygame
from constants import screen, monogram, white

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.font = monogram
        self.surf = self.font.render(f"Current Score: {self.score}", False, white)
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y
    
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def update(self, num):
        self.score += num
    
    def render(self):
        self.surf = self.font.render(f"Score: {self.score}", False, white)
        screen.blit(self.surf, (self.x, self.y))

    def reset(self):
        self.score = 0
        