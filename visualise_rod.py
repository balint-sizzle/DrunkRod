import pygame as pg
import pymunk as pm
import pymunk.pygame_util as pmg
from rod_sim import Jack
from math import atan2

class RodDraw(Jack):
    def __init__(self):
        pg.init()
        canvas = pg.display.set_mode((800,800))
        self.draw_options = pmg.DrawOptions(canvas)

        self.jack_rod = Jack()
        canvas.fill(pg.Color("Grey"))
            
    def draw(self):
        self.jack_rod.space.debug_draw(self.draw_options)
        pg.display.flip()
    
    def kill(self):
        pg.quit()
        exit()
