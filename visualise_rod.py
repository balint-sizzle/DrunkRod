import pygame as pg
import pymunk as pm
import gzip
import neat
import pymunk.pygame_util as pmg
from rod_sim import Jack
from math import atan2
import pickle

class RodDraw(Jack):
    def __init__(self):
        pg.init()
        self.canvas = pg.display.set_mode((800,800))
        self.draw_options = pmg.DrawOptions(self.canvas)
        checkp = neat.Checkpointer(filename_prefix="checkpoints/neat-checkpoint-")
        #p = checkp.restore_checkpoint('checkpoints/neat-checkpoint-729')
        config = neat.config.Config(neat.DefaultGenome,
                                        neat.DefaultReproduction,
                                        neat.DefaultSpeciesSet,
                                        neat.DefaultStagnation,
                                        "config.ini")
        stats = neat.StatisticsReporter()
        with gzip.open("checkpoints/neat-checkpoint-"+"265") as f:
            generation, config, population, species_set, rndstate = pickle.load(f)
            print(population.best_genome)
            nn = neat.nn.FeedForwardNetwork.create(population.best_genome, config)
            self.jack_rod = Jack()
            while not self.jack_rod.fallen:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        raise SystemExit
                    if pg.key.get_pressed()[pg.K_RIGHT]:
                        self.jack_rod.circle_b.position = (self.jack_rod.circle_b.position.x+300, self.jack_rod.circle_b.position.y)
                    if pg.key.get_pressed()[pg.K_LEFT]:
                        self.jack_rod.circle_b.position = (self.jack_rod.circle_b.position.x-300, self.jack_rod.circle_b.position.y)
                output = nn.activate([self.jack_rod.get_angle()])[-1]
                self.jack_rod.add_velocity(output * 10)
                self.jack_rod.move_base()
                self.draw()

    def draw(self):
        self.canvas.fill(pg.Color("Grey"))
        self.jack_rod.space.debug_draw(self.draw_options)
        #print(self.jack_rod.base_b.position, end="\r", flush=True)
        pg.display.flip()
a = RodDraw()