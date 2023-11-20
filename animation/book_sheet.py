import pygame
import os
from multirow_sheet import multirowSheet as SpriteSheet
from constants import black
from random import choice

# get frames takes num_frames, num_rows, width, height, scale, colour, start_x, start_y

def random_book():
    books_list = []
    files = os.listdir("assets/books/")
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    books_list.extend(image_files)
    return choice(books_list)


def get_all_animations():
    book = random_book()
    filepath = "assets/books/"+book
    book_pick = pygame.image.load(filepath).convert_alpha()
    run_animation = SpriteSheet(book_pick)
    run_animation.get_frames(6, 1, 32, 32, 2, black, 0,0)

    book_animations = {
        "run_right": run_animation.frames,
    }
    return book_animations

book_animations = get_all_animations()



    