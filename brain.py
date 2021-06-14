###
# input: angle
# output: movement
# fitness: time alive

from __future__ import print_function
import os
import neat
import visualize
from rod_sim import Jack

config = neat.config.Config(neat.DefaultGenome,
                            neat.DefaultReproduction,
                            neat.DefaultSpeciesSet,
                            neat.DefaultStagnation,
                            "config.ini")

sigmoid_scaling_factor = 100

def eval_genome(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        jack = Jack()
        while jack.time_elapsed < 10 and not jack.fallen:
            output = net.activate(jack.get_angle())
            jack.move_base(output * sigmoid_scaling_factor)
        genome.fitness = jack.time_elapsed

def run)
population = neat.Population(config)

