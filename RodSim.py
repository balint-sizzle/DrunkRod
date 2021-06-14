import pymunk as pm
from math import atan2
from math import pi


class Jack:
    fallen = False
    base_w, base_h = 600, 20
    step_size = 1/50
    time_elapsed = 0

    def __init__(self):
        space = pm.Space()

        space._set_gravity((0,100))
        base_b = pm.Body(1, 100, body_type=pm.Body.KINEMATIC)
        circle_b = pm.Body(1, 1, body_type=pm.Body.DYNAMIC)

        base_b.position = (400, 500)
        circle_b.position = (400, 320)

        joint = pm.PinJoint(circle_b, base_b, (0, 0), (0, -self.base_h/2))
        base = pm.Poly(base_b, self.rect_shape(self.base_w, self.base_h))
        circle = pm.Circle(circle_b, 1)

        space.add(circle_b, circle)
        space.add(base_b, base)
        space.add(joint)

        self.fallen = False

    def get_angle(self):
        b2 = self.circle
        b1 = self.base
        return round((atan2(b2.position.y-b1.position.y,
                            b2.position.x-b1.position.x) *180/pi) + 90, 3)

    def step_rod(self):
        self.space.step(self.step_size)
        self.time_elapsed += self.step_size

        return self.get_angle()
    
    @staticmethod
    def rect_shape(w, h):
        return [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]
    @staticmethod
    def move_body(amnt, poly):
        poly.body.position = (poly.body.position.x+amnt, poly.body.position.y)