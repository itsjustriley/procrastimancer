import pygame
from spritesheet import SpriteSheet

class multirowSheet(SpriteSheet):
    def __init__(self, image):
        super().__init__(image)
    
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (0, ((frame % 4) * height), width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        return image
    
    def get_frames(self, num_frames, num_rows, width, height, scale, colour, start_x, start_y):
        for row in range(num_rows):
            for column in range(num_frames//num_rows):
                image = pygame.Surface((width,height)).convert_alpha()
                image.blit(self.sheet,(0,0), (start_x+(width*column), start_y+(height*row), width, height))
                image = pygame.transform.scale(image, (scale*width, scale*height))
                image.set_colorkey(colour)
                self.frames.append(image)