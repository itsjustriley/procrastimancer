import pygame
from constants import monogram, white, screen, screen_width, screen_height

class StartScreen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.font = monogram
        self.highscore = 0
        self.surf = self.font.render(f" * P R O C R A S T I M A N C E R * ", False, white)
        self.surfHello = self.font.render(f"Hello, Witchling!", False, white)
        self.surfLife = self.font.render(f"Life is hard. Take some time to recharge.", False, white)
        self.surfCats = self.font.render(f"Cuddle your cats (+100)", False, white)
        self.surfTreats = self.font.render(f"Have a treat(+50)", False, white)
        self.surfTea = self.font.render(f"Enjoy your tea before it gets cold, (+200)", False, white)
        self.surfOops = self.font.render(f"Don't let cats spill your tea. (-200)", False, white)
        self.surfOops2 = self.font.render(f"They'll also eat your treats.", False, white)
        self.surfHomework = self.font.render(f"Avoid your homework at all costs.", False, white)
        self.surfMove = self.font.render(f"Use your arrow keys to move.", False, white)
        self.surfPause = self.font.render(f"Press space to pause.", False, white)
        self.surfExit = self.font.render(f"Press escape to exit.", False, white)
        self.surfStart = self.font.render(f"Press enter to start.", False, white)
        self.all_surfs = [self.surf, self.surfHello, self.surfLife, self.surfCats, self.surfTreats, self.surfTea, self.surfOops, self.surfOops2, self.surfHomework, self.surfMove, self.surfPause, self.surfExit, self.surfStart]
        self.dx = 0
        self.dy = 0
        self.visible = True
        self.text_width = self.surf.get_width()
        self.text_height = self.surf.get_height()
        self.x = screen_width/2 - self.text_width/2
        self.y = screen_height/2 - self.text_height/2


    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def render(self):
        if self.visible == True:
            pygame.draw.rect(screen, pygame.Color(0,0,0,5), pygame.Rect(screen_width//10, screen_width//10, screen_width-screen_width//5, screen_width-screen_width//5))
            #screen.blit(self.surf, (self.x, self.y))
            y = self.y - len(self.all_surfs)/2 * 35
            for s in self.all_surfs:
                x = screen_width/2 - s.get_width()/2
                screen.blit(s, (x, y))
                y += 35
            

    def reset(self):
        self.visible = False