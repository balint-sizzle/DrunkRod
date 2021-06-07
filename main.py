import pymunk as pm
import pygame as pg
from pygame import gfxdraw
import pymunk.pygame_util as pmg
pg.init()
canvas = pg.display.set_mode((800,800))
clock = pg.time.Clock()
space = pm.Space()



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

def add_force(poly):
    poly.body.apply_impulse_at_world_point((10,0), (400,400))

def move_left(poly):
    poly.body.position = (poly.body.position.x-10, poly.body.position.y)
    pm.Body.update_position(poly.body, 0.1)

space._set_gravity((0,100))

rod_w, rod_h = 10, 100
base_w, base_h = 200, 20

rod_b = pm.Body(10, 1, body_type=pm.Body.DYNAMIC)
base_b = pm.Body(1, 1, body_type=pm.Body.STATIC)

rod_b.position = (400, 380)
base_b.position = (400, 400)


rod = pm.Poly(rod_b, rect_shape(rod_w, rod_h))
base = pm.Poly(base_b, rect_shape(base_w, base_h))

rod.elasticity=0.0
base.elasticity=0.0
# rod.friction = 1
# base.friction = 1

#space.add_default_collision_handler()

space.add(base_b, base)
space.add(rod_b, rod)


print(base.collision_type)
print(rod.bb)

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                add_force(rod)
            if event.key == pg.K_UP:
                add_force(base)
            if event.key == pg.K_LEFT:
                move_left(base)
        if event.type == pg.QUIT:
            pg.quit()

    x = int(rod.body.position.x)
    y = int(rod.body.position.y)
    canvas.fill(pg.Color("Grey"))
    draw_rect(rod)
    draw_rect(base)
    pg.display.flip()
    space.step(1/500)