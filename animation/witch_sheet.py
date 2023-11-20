import pygame
from spritesheet import SpriteSheet
from constants import black
# get_image takes frame, width, height, scale, color
# get_frames takes num_frames, width, height, scale, color

idle_image = pygame.image.load("assets/Blue_witch/B_witch_idle.png").convert_alpha()
idle_animation = SpriteSheet(idle_image)
idle_animation.get_frames(6, 32, 48, 2, black)

run_image = pygame.image.load("assets/Blue_witch/B_witch_run.png").convert_alpha()
run_animation = SpriteSheet(run_image)
run_animation.get_frames(8, 32, 48, 2, black)

death_image = pygame.image.load("assets/Blue_witch/B_witch_death.png").convert_alpha()
death_animation = SpriteSheet(death_image)
death_animation.get_frames(12, 32, 48, 2, black)

revive_animation = death_animation.frames[::-1]

charge_image = pygame.image.load("assets/Blue_witch/B_witch_charge.png").convert_alpha()
charge_animation = SpriteSheet(charge_image)
charge_animation.get_frames(5, 48, 48, 2, black)

witch_animations = {
    "idle": idle_animation.frames,
    "run": run_animation.frames,
    "death": death_animation.frames,
    "charge": charge_animation.frames,
    "revive": revive_animation
}