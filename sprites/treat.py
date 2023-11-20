import pygame
from GameObject import GameObject
from random import choice
from constants import lanes, black, screen, frame_rate
import os

treat_images = []
width = 32
height = 32

treat_folder = "assets/treats/"
treat_files = [file for file in os.listdir(treat_folder)]
for file in treat_files:
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(pygame.image.load(treat_folder+file), (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width, height))
    image.set_colorkey(black)
    treat_images.append(image)

images = {
    "tea": [pygame.image.load("assets/tea.png")],
    "treat": treat_images
}

class Treat(GameObject):
    def __init__(self):
        super().__init__(0, 0, images)
        self.dy = 0
        self.dx = 0
        self.speed = 0
        self.state = "tea"
        self.points = 200
        self.frame_delay = frame_rate*30
        self.reset()   

    def reset(self):
        self.tea_or_treat()
        self.x = choice(lanes)
        self.y = choice(lanes)
        self.dx = 0
        self.dy = 0

    def render(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.frame_delay -= 1
        if self.frame_delay <= 0:
            self.reset()
        screen.blit(self.surf, (self.x, self.y))

    def move(self):
        pass
        
    def tea_or_treat(self):
        self.state = choice(["tea", "treat"])
        if self.state == "treat":
            self.image = choice(self.animations[self.state])
            self.points = 50
            self.frame_delay = frame_rate*10000
        else: 
            self.image = self.animations[self.state][0]
            self.points = 200
            self.frame_delay = frame_rate*10
        self.surf = self.image

    



