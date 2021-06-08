import pymunk as pm
import pygame as pg
from pygame import gfxdraw
import pymunk.pygame_util as pmg

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
    poly.body.position = (poly.body.position.x-100, poly.body.position.y)
    pm.Body.update_position(poly.body, 0.1)

def move_right(poly):
    poly.body.position = (poly.body.position.x+100, poly.body.position.y)
    pm.Body.update_position(poly.body, 0.1)

space._set_gravity((0,100))

rod_w, rod_h = 10, 100
base_w, base_h = 200, 20
base_b_w, base_b_h = 2000, 20

rod_b = pm.Body(1, 1, body_type=pm.Body.DYNAMIC)
base_b = pm.Body(1, 100, body_type=pm.Body.DYNAMIC)
base_base_b = pm.Body(1, 100, body_type=pm.Body.STATIC)
#joint = pm.PinJoint(rod_b, base_b, (0, -100), (0, -11))
#joint._set_distance(10)

rod_b.position = (400, 400-rod_h/2)
base_b.position = (400, 400+base_h/2)
base_base_b.position = (400, 410+base_h/2+base_b_h/2)

rod = pm.Poly(rod_b, rect_shape(rod_w, rod_h))
base = pm.Poly(base_b, rect_shape(base_w, base_h))
base_base = pm.Poly(base_base_b, rect_shape(base_b_w, base_b_h))

rod.friction = 1
base.friction = 1
base_base.friction = 10
rod_b.elasticity = 0.0
base_b.elasticity = 0.0
base_base_b.elasticity = 0.0
#space.add_default_collision_handler()

space.add(base_b, base)
space.add(rod_b, rod)
space.add(base_base_b, base_base)
#space.add(joint)


while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                pass
                #add_force(rod)
            if event.key == pg.K_UP:
                pass
            if event.key == pg.K_LEFT:
                add_force_LEFT(base)
            if event.key == pg.K_RIGHT:
                add_force_RIGHT(base)
        if event.type == pg.QUIT:
            pg.quit()

    canvas.fill(pg.Color("Grey"))
    
    space.step(1/500)

    space.debug_draw(draw_options)
    pg.display.flip()
    