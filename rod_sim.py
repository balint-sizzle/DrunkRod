import pymunk as pm
import random
from math import atan2
from math import pi


class Jack:
    fallen = False
    base_w, base_h = 600, 20
    step_size = 1/500
    time_elapsed = 0

    def __init__(self):
        self.space = pm.Space()

        self.space._set_gravity((0,100))
        self.base_b = pm.Body(1, 100, body_type=pm.Body.KINEMATIC)
        self.circle_b = pm.Body(1, 1, body_type=pm.Body.DYNAMIC)

        spice_factor = random.choice([-200, -150, -100, 100, 150, 200])
        self.base_b.position = (400+spice_factor, 500)
        self.circle_b.position = (400, 320)

        joint = pm.PinJoint(self.circle_b, self.base_b, (0, 0), (0, -self.base_h/2))
        self.base = pm.Poly(self.base_b, self.rect_shape(self.base_w, self.base_h))
        self.circle = pm.Circle(self.circle_b, 1)

        self.space.add(self.circle_b, self.circle)
        self.space.add(self.base_b, self.base)
        self.space.add(joint)

        self.fallen = False

    def get_angle(self):
        b2 = self.circle_b
        b1 = self.base_b
        return round((atan2(b2.position.y-b1.position.y,
                            b2.position.x-b1.position.x) *180/pi) + 90, 3)

    def move_base(self, delta_p):
        self.move_body(delta_p)
        
        self.space.step(self.step_size)
        self.time_elapsed += self.step_size

        return self.get_angle()
    
    def move_body(self, amnt):
        self.base_b.position = (self.base_b.position.x+amnt, self.base_b.position.y)

    @staticmethod
    def rect_shape(w, h):
        return [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]