import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
from constants import clock, screen, background, tile_background, background_music, lose_sound, max_books, new_book_score
from sprites.player import Player
from sprites.scoreboard import ScoreBoard
from sprites.cat import Cat
from sprites.book import Book
from sprites.gameOverScreen import GameOverScreen
from random import choice
from sprites.startScreen import StartScreen
from sprites.treat import Treat
import os
from sprites.light import Light


paused = True
game_started = False
cat_count = 0

sound = pygame.mixer.Sound(background_music)  
sound.play(loops=-1)

# Called when the player collides with a book
def game_over():
    for sprite in moving_sprites:
        sprite.kill()
        sprite.reset()
    pygame.mixer.stop()
    lose = pygame.mixer.Sound(lose_sound)
    lose.play()
    # update high score if necessary
    if scoreboard.score > end_screen.highscore:
        end_screen.update(scoreboard.score)
    player.state = "death"
    player.controlled = False
    scoreboard.kill()
    hideTreat(treat)
    

    end_screen.visible=True

def new_game():
    player.reset()
    player.immune = True
    end_screen.visible=False
    scoreboard.reset()
    player.state = "revive"
    player.frame = 0
    sound.play(loops=-1)
    treat.frame_delay=180
    pygame.time.set_timer(pygame.USEREVENT, 5000)

def hideTreat(t):
    t.x = -1000
    t.y = -1000
    t.frame_delay = 1000000

player = Player()
cat = Cat()
book = Book()
books = pygame.sprite.Group()
start_screen = StartScreen(0,0)
treat = Treat()
scoreboard = ScoreBoard(10, 10)
end_screen = GameOverScreen(0,0)
light1 = Light()
light2 = Light()
light3 = Light()
light4 = Light()



cat_sounds = []
for file in os.listdir("assets/cat_sounds"):
    cat_sounds.append(pygame.mixer.Sound(f"assets/cat_sounds/{file}"))

all_sprites = pygame.sprite.Group()
cats = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
moving_sprites = pygame.sprite.Group()
lights = pygame.sprite.Group()

def reset_sprite_lists():
    all_sprites.add(player, book, scoreboard, cat, end_screen, light1, light2, light3, light4)
    cats.add(cat)
    moving_sprites.add(cat, book)
    books.add(book)
    lights.add(light1, light2, light3, light4)

reset_sprite_lists()
all_sprites.add(start_screen)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif (event.type == pygame.USEREVENT):
            player.immune = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                running = False
            elif ((event.key == pygame.K_RETURN) or (event.key == pygame.K_SPACE)) and game_started!=True:
                game_started = True
                paused = False
                player.controlled = True
                start_screen.kill()
                all_sprites.add(treat)
            elif (event.key == pygame.K_SPACE):
                if player.state == "death":
                    new_game()
                else:
                    paused = False if paused else True
                    player.controlled = not paused
            if player.controlled == False:
                pass    
            elif (event.key == pygame.K_LEFT):
                player.left()
            elif (event.key == pygame.K_RIGHT):
                player.right()
            elif (event.key == pygame.K_UP):
                player.up()
            elif (event.key == pygame.K_DOWN):
                player.down()


    screen.fill(background)
    tile_background()

    for sprite in all_sprites:
        if not paused:
            sprite.move()
        sprite.render()
    
    if player.respawned == True:
        reset_sprite_lists()
        player.respawned=False

    if player.immune == False:    
        caught_cat = pygame.sprite.spritecollideany(player, cats)
        if caught_cat:
            if pygame.sprite.collide_circle(player, cat):
                cat_sound = choice(cat_sounds)
                cat_sound.play()
                player.cat_collected()
                scoreboard.update(100)
                cat_count += 1
                if cat_count % 10 == 0:
                    if len(books)<max_books:
                        new_book = Book()
                        all_sprites.add(new_book)
                        moving_sprites.add(new_book)
                        books.add(new_book)
                for sprite in moving_sprites:
                    sprite.speed = sprite.set_speed(scoreboard.score)
                cat.reset()
            
        if game_started==True:
            book_hit = pygame.sprite.spritecollideany(player, books)
            for sprite in books:
                if book_hit and player.state != 'death' and player.state != 'revive':
                    if pygame.sprite.collide_circle(player, sprite):
                        game_over()

            if pygame.sprite.collide_circle(player, treat):
                scoreboard.update(treat.points)
                treat.reset()

            if pygame.sprite.collide_circle(cat, treat):
                if treat.state == "tea":
                    splash = pygame.mixer.Sound("assets/splash.mp3")
                    splash.play()
                    scoreboard.update(-treat.points)
                else: 
                    crunch = pygame.mixer.Sound("assets/eat.mp3")
                    crunch.play()
                treat.reset()
    
        
    pygame.display.flip()

    clock.tick(60)

