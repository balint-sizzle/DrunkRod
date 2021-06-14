import pygame as pg
import pymunk as pm
import pymunk.pygame_util as pmg
from rod_sim import Jack
from math import atan2

class RodDraw(Jack):
    def __init__(self):
        pg.init()
        self.canvas = pg.display.set_mode((800,800))
        self.draw_options = pmg.DrawOptions(self.canvas)

        self.jack_rod = Jack()

    def draw(self):
        self.canvas.fill(pg.Color("Grey"))
        self.jack_rod.space.debug_draw(self.draw_options)
        print(self.jack_rod.base_b.position)
        pg.display.update()
    
    def kill(self):
        pg.quit()