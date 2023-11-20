import pygame




background = (0, 10, 15)

black = (0, 0, 0)
white = (255, 255, 255)

background_music = "assets/JDSherbert - Minigame Music Pack - Digital Waves.wav"
lose_sound = "assets/lose.mp3"

frame_rate = 15

clock = pygame.time.Clock()

screen_width = 740
screen_height = 740

floor_tile = pygame.image.load("assets/floortile.jpeg")
floor_tile = pygame.transform.scale(floor_tile, (screen_width//5,screen_height//5))
floor_tile.set_alpha(25)

max_books = 5
new_book_score = 10

sprite_width = 64

left_top_bound = 0 - sprite_width
right_bottom_bound = screen_width

screen = pygame.display.set_mode((screen_width, screen_height))

def generate_lanes(num_lanes):
    temp_lanes = []
    for i in range(num_lanes):
        temp_lanes.append((i+1)*(screen_width/(num_lanes)) - (screen_width/(num_lanes))/2 - sprite_width//2)
    return temp_lanes

def tile_background():
    for i in range(5):
        for j in range(5):
            screen.blit(floor_tile, (i*screen_width//5, j*screen_height//5))

lanes = generate_lanes(5)

monogram = pygame.font.Font("assets/monogram-extended.ttf", 30)