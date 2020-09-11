import numpy as np
from itertools import product
from dataclasses import dataclass, field

class Pitch:
    def get_intersections(self):
        intersection_points = list(product(self.vert_lines.keys(), self.horiz_lines.keys()))
        intersections = {'_'.join([vl, hl]): (self.vert_lines[vl], self.horiz_lines[hl])
                        for vl, hl in intersection_points}
        
        return intersections

@dataclass
class FootballPitch(Pitch):
    SCALE: int = 5
    X_SIZE: int = 105
    Y_SIZE: int = 68
    GOAL: float = field(default=7.32, init=False)
    BOX_HEIGHT: float = field(default=16.5*2+7.32, init=False)
    BOX_WIDTH: float = field(default=16.5, init=False)
    GOAL_AREA_WIDTH: float = field(default=5.5, init=False)
    GOAL_AREA_HEIGHT: float = field(default=5.5*2+7.32, init=False)

    def __post_init__(self):
        self.vert_lines = {'LG': 0,
                           'LGA': self.GOAL_AREA_WIDTH,
                           'LPA': self.BOX_WIDTH,
                           'HW': self.X_SIZE/2,
                           'RPA': self.X_SIZE-self.BOX_WIDTH,
                           'RGA': self.X_SIZE-self.GOAL_AREA_WIDTH,
                           'RG': self.X_SIZE
                           }

        self.horiz_lines =  {'DG': self.BOX_HEIGHT,
                             'UP': (self.Y_SIZE-self.BOX_HEIGHT)/2,
                             'UG': (self.Y_SIZE-self.GOAL_AREA_HEIGHT)/2,
                             'DG': (self.Y_SIZE+self.GOAL_AREA_HEIGHT)/2,
                             'DP': (self.Y_SIZE+self.BOX_HEIGHT)/2,
                             'U': 0,
                             'D': self.Y_SIZE,
                             'C': self.Y_SIZE/2
                             }


    def get_penalty_area(self):
        SPACE = (self.Y_SIZE-self.BOX_HEIGHT)/2
        PENALTY_AREA = [[self.BOX_WIDTH, SPACE],
                        [self.BOX_WIDTH, self.BOX_HEIGHT+SPACE],
                        [0, SPACE],
                        [0, self.BOX_HEIGHT+SPACE]
                       ]

        return np.array(PENALTY_AREA)*self.SCALE