from colorsets import COLORSETS


class Level:
    def __init__(self, name, colorset, wall_boxes=[], named_wall_boxes={}, buttons={}, starting_point=(), hole=()):
        self.name = name
        self.colorset = colorset
        self.bg_color = COLORSETS[self.colorset]["bg"]
        self.wall_color = COLORSETS[self.colorset]["wall"]
        self.ball_color = COLORSETS[self.colorset]["ball"]
        self.obj_color = COLORSETS[self.colorset]["obj"]
        self.wall_boxes = wall_boxes
        self.named_wall_boxes = named_wall_boxes
        self.buttons = buttons
        self.starting_point = starting_point
        self.hole = hole
