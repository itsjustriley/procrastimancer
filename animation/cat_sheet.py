import pygame
import os
from multirow_sheet import multirowSheet as SpriteSheet
from constants import black
from random import choice

# get frames takes num_frames, num_rows, width, height, scale, colour, start_x, start_y

def random_cat():
    cats_list = []
    files = os.listdir("assets/cats/")
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    cats_list.extend(image_files)
    return choice(cats_list)


def get_all_animations():
    cat = random_cat()
    filepath = "assets/cats/"+cat
    kitty = pygame.image.load(filepath).convert_alpha()
    run_right_animation = SpriteSheet(kitty)
    run_right_animation.get_frames(8, 2, 32, 32, 2, black, 640, 480)

    run_up_animation = SpriteSheet(kitty)
    run_up_animation.get_frames(8, 2, 32, 32, 2, black, 640, 288)

    run_down_animation = SpriteSheet(kitty)
    run_down_animation.get_frames(8, 2, 32, 32, 2, black, 640, 32)

    cat_animations = {
        "run_right": run_right_animation.frames,
        "run_up": run_up_animation.frames,
        "run_down": run_down_animation.frames
    }
    return cat_animations

cat_animations = get_all_animations()



    