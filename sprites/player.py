from GameObject import GameObject
from constants import lanes
from animation.witch_sheet import witch_animations


class Player(GameObject):
    def __init__(self):
        super().__init__(0, 0, witch_animations)
        self.dy = 0
        self.dx = 0
        self.pos_x = 0
        self.pos_y = 0
        self.state = "idle"
        self.controlled = False
        self.reset()
        

    def update_dx_dy(self):
        if self.dx > 1 or self.dx < -1 or self.dy > 1 or self.dy < -1:
            self.state = "run"
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]
    
    def left(self):
        self.facing = "left"
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        self.facing = "right"
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()
    
    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * .25
        self.y -= (self.y - self.dy) * .25
        
    
    def reset(self):
        self.pos_x = len(lanes) // 2
        self.pos_y = len(lanes) // 2
        self.x = lanes[self.pos_x] 
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def cat_collected(self):
        self.state = "charge"
        self.frame = 0
        self.frame_delay = 5
