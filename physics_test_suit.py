import pymunk as pm
import pymunk.pygame_util as pmg
import random
from math import atan2
from math import sqrt
from math import pi
import pygame as pg

class Jack:
    fallen = False
    base_w, base_h = 600, 20
    step_size = 1/500
    time_elapsed = 0
    max_vel = .05
    velocity = 0
    vel_falloff = 0.01

    def __init__(self):
        self.space = pm.Space()
        

        self.space._set_gravity((0,1000))
        self.base_b = pm.Body(1, 100, body_type=pm.Body.KINEMATIC)
        self.circle_b = pm.Body(1, 1, body_type=pm.Body.DYNAMIC)

        spice_factor = random.choice([-200, -150, -100, 100, 150, 200])
        self.base_b.position = (100, 500)
        self.circle_b.position = (400, 320)

        joint = pm.PinJoint(self.circle_b, self.base_b, (0, 0), (0, -self.base_h/2))
        self.base = pm.Poly(self.base_b, self.rect_shape(self.base_w, self.base_h))
        self.circle = pm.Circle(self.circle_b, 1)

        self.base_b.velocity_func = zero_gravity

        self.space.add(self.circle_b, self.circle)
        self.space.add(self.base_b, self.base)
        self.space.add(joint)

        self.fallen = False

    def get_angle(self):
        b2 = self.circle_b
        b1 = self.base_b
        return round((atan2(b2.position.y-b1.position.y,
                            b2.position.x-b1.position.x) *180/pi) + 90, 3)

    def move_base(self):
        self.move_body()
        self.take_time_step()
        return self.get_angle()
    
    def take_time_step(self):
        self.space.step(self.step_size)
        self.velocity *= 1- self.vel_falloff
        self.time_elapsed += self.step_size
    
    def move_body(self):
        self.base_b.position = (self.base_b.position.x+self.velocity, self.base_b.position.y)

    def add_velocity(self, vel):
        self.velocity += vel*self.max_vel
    
    @staticmethod
    def rect_shape(w, h):
        return [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]


def draw():
        canvas.fill(pg.Color("Grey"))
        jack_rod.space.debug_draw(draw_options)
        #print(self.jack_rod.base_b.position, end="\r", flush=True)
        pg.display.flip()
    
def zero_gravity(body, gravity, damping, dt):
    pm.Body.update_velocity(body, (0,-100), damping, dt)

pg.init()
canvas = pg.display.set_mode((800,800))
draw_options = pmg.DrawOptions(canvas)

jack_rod = Jack()

while not jack_rod.fallen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if pg.key.get_pressed()[pg.K_LEFT]:
            jack_rod.move_body()
        if pg.key.get_pressed()[pg.K_RIGHT]:
            jack_rod.move_body()
        if pg.key.get_pressed()[pg.K_d]:
            jack_rod.add_velocity(10)
        if pg.key.get_pressed()[pg.K_a]:
            jack_rod.add_velocity(-10)
        
    #output = nn.activate([jack_rod.get_angle()])[-1]
    jack_rod.move_base()
    draw()