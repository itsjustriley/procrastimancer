import pygame
from constants import monogram, white, screen, screen_width, screen_height

class GameOverScreen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.font = monogram
        self.highscore = 0
        self.surf = self.font.render(f"Game Over!", False, white)
        self.surf2 = self.font.render(f"High Score: {self.highscore}", False, white)
        self.surf3 = self.font.render(f"Press SPACE to Play Again", False, white)
        self.dx = 0
        self.dy = 0
        self.visible = False
        self.text_width = self.surf.get_width()
        self.text_height = self.surf.get_height()
        self.x = screen_width/2 - self.text_width/2
        self.y = screen_height/2 - self.text_height/2


    def move(self):
        self.x += self.dx
        self.y += self.dy

    def update(self, hs):
        self.highscore = hs
        self.surf2 = self.font.render(f"High Score: {self.highscore}", False, white)
        
    def render(self):
        if self.visible == True:
            pygame.draw.rect(screen, pygame.Color(0,0,0,50), pygame.Rect(screen_width/4, screen_width/4, screen_width/2, screen_height/2))
            #screen.blit(self.surf, (self.x, self.y))
            y = self.y - 35
            for s in [self.surf, self.surf2, self.surf3]:
                x = screen_width/2 - s.get_width()/2
                screen.blit(s, (x, y))
                y += 35
            

    def reset(self):
        self.visible = False