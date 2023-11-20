from GameObject import GameObject
from animation.cat_sheet import cat_animations, get_all_animations
from random import choice
from constants import lanes, right_bottom_bound, sprite_width

class Cat(GameObject):
    def __init__(self,):
        super().__init__(0, 0, cat_animations)
        self.dy = 0
        self.dx = 0
        self.speed = self.set_speed(0)
        self.state = 0
        self.reset()

    def reset(self):
        self.speed = self.set_speed(0)
        v_or_h = choice(['v', 'h'])
        lane = choice(lanes)
        speed_choice = choice([self.speed, -self.speed])
        if v_or_h == 'v':
            self.x = lane
            self.dy = speed_choice
            self.dx = 0
            self.y = -sprite_width if self.dy > 0 else right_bottom_bound
            self.state = "run_down" if self.dy > 0 else "run_up"
        else:
            self.y = lane
            self.dx = speed_choice
            self.dy = 0
            self.x = -sprite_width if self.dx > 0 else right_bottom_bound
            self.state = "run_right"
            self.facing = "left" if self.dx < 0 else "right"
        self.animations = get_all_animations()
        #print('The state of this cat is '+str(self.state))

