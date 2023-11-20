from GameObject import GameObject
from animation.book_sheet import book_animations, get_all_animations
from random import choice
from constants import lanes, right_bottom_bound, sprite_width

class Book(GameObject):
    def __init__(self,):
        super().__init__(0, 0, book_animations)
        self.dy = 0
        self.dx = 0
        self.speed = self.set_speed(0)
        self.state = "run_right"
        self.reset()

    def reset(self):
        self.animations = get_all_animations()
        self.speed = self.set_speed(0)
        v_or_h = choice(['v', 'h'])
        lane = choice(lanes)
        speed_choice = choice([self.speed, -self.speed])
        if v_or_h == 'v':
            self.x = lane
            self.dy = speed_choice
            self.dx = 0
            self.y = -sprite_width if self.dy > 0 else right_bottom_bound
        else:
            self.y = lane
            self.dx = speed_choice
            self.dy = 0
            self.x = -sprite_width if self.dx > 0 else right_bottom_bound
            self.facing = "left" if self.dx < 0 else "right"

