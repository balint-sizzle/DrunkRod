import pymunk as pm
import pygame as pg
from pygame import gfxdraw
import pymunk.pygame_util as pmg
from math import atan2

pg.init()
canvas = pg.display.set_mode((800,800))
clock = pg.time.Clock()
space = pm.Space()
draw_options = pmg.DrawOptions(canvas)


def rect_shape(w, h):
    return [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]

def draw_text(pos):
    font = pg.font.SysFont("Ariel", 100)
    thing = font.render("my dad", 1, (255,255,255))
    canvas.blit(thing, (pos[0]-100, pos[1]-50))

def draw_rect(shape):
    verts = []
    for v in shape.get_vertices():
        x = v.rotated(shape.body.angle)[0] + shape.body.position[0]
        y = v.rotated(shape.body.angle)[1] + shape.body.position[1]
        verts.append((x, y))
    gfxdraw.filled_polygon(canvas, verts, pg.Color("Red"))

def add_force_LEFT(poly):
    poly.body.apply_impulse_at_local_point((-1000,0), (0,0))
def add_force_RIGHT(poly):
    poly.body.apply_impulse_at_local_point((1000,0), (0,0))

def move_left(poly):
    poly.body.position = (poly.body.position.x-1, poly.body.position.y)
    pm.Body.update_position(poly.body, 0.1)

def move_right(poly):
    poly.body.position = (poly.body.position.x+1, poly.body.position.y)
    pm.Body.update_position(poly.body, 0.1)

def get_angle(b1, b2):
    return round((atan2(b2.position.y-b1.position.y, b2.position.x-b1.position.x)*180/3.141) + 90, 3)
space._set_gravity((0,100))

base_w, base_h = 600, 20
base_b = pm.Body(1, 100, body_type=pm.Body.KINEMATIC)
circle_b = pm.Body(1, 1, body_type=pm.Body.DYNAMIC)

base = pm.Poly(base_b, rect_shape(base_w, base_h))
circle = pm.Circle(circle_b, 1)

base_b.position = (400, 500)
circle_b.position = (400, 320)

joint = pm.PinJoint(circle_b, base_b, (0, 0), (0, -base_h/2))

space.add(circle_b, circle)
space.add(base_b, base)
space.add(joint)
print(circle.body.position)

while 1:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                pass
                #add_force(rod)
            if event.key == pg.K_UP:
                pass
            if event.key == pg.K_LEFT:
                move_left(base)
            if event.key == pg.K_RIGHT:
                move_right(base)
        if event.type == pg.QUIT:
            pg.quit()

    canvas.fill(pg.Color("Grey"))
    
    space.step(1/50)
    print(get_angle(base.body, circle.body))

    space.debug_draw(draw_options)

    pg.display.flip()
