import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        self.frames = []
    
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (0, (frame * height), width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        return image

    def get_frames(self, num_frames, width, height, scale, color):
        for i in range(num_frames):
            self.frames.append(self.get_image(i, width, height, scale, color))

