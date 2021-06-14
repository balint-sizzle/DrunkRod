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


