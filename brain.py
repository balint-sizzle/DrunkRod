###
# input: angle
# output: movement
# fitness: time alive

import neat


config = neat.config.Config(neat.DefaultGenome,
                            neat.DefaultReproduction,
                            neat.DefaultSpeciesSet,
                            neat.DefaultStagnation,
                            "config.ini")

def eval_genome(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        time_elapsed = 0
        while 
        net.activate(angle)
        genome.fitness -= (output[0] - xo[0]) ** 2
population = neat.Population(config)

