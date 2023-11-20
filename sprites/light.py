from GameObject import GameObject
from random import choice, randint
from constants import lanes, right_bottom_bound, sprite_width, black, screen
import os
import pygame

lights = []
light_folder = "assets/lights/"
width = 400
height = 400
light_files = [file for file in os.listdir(light_folder)]
for file in light_files:
    pic = pygame.image.load(light_folder+file)
    image = pygame.Surface((width, height))
    image.blit(pic, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (16, 16))
    image.set_colorkey(black)
    lights.append(image)

lighting = {
    "run_right": lights
}


class Light(GameObject):
    def __init__(self,):
        super().__init__(0, 0, lighting)
        self.dy = 0
        self.dx = 0
        self.speed = 1
        self.state = "run_right"
        self.reset()

    def reset(self):
        self.image = choice(self.animations[self.state])
        self.surf = self.image
        start = choice(["left", "right", "top", "bottom"])
        start_position = -sprite_width
        other_axis = randint(0, right_bottom_bound)
        start_delta = self.speed
        other_axis_delta = randint(-self.speed, self.speed)
        if start == "left":
            self.x = start_position
            self.y = other_axis
            self.dx = start_delta
            self.dy = other_axis_delta
        elif start == "right":
            self.x = right_bottom_bound
            self.y = other_axis
            self.dx = -start_delta
            self.dy = other_axis_delta
        elif start == "top":
            self.x = other_axis
            self.y = start_position
            self.dx = other_axis_delta
            self.dy = start_delta
        else:
            self.x = other_axis
            self.y = right_bottom_bound
            self.dx = other_axis_delta
            self.dy = -start_delta


    def render(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.surf.set_alpha(20)
        screen.blit(self.surf, (self.x, self.y))