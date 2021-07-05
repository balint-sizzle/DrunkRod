import pickle
import gzip
import neat

prefix = "checkpoints/neat-checkpoint-"
config = neat.config.Config(neat.DefaultGenome,
                                        neat.DefaultReproduction,
                                        neat.DefaultSpeciesSet,
                                        neat.DefaultStagnation,
                                        "config.ini")
with gzip.open(prefix+"1000") as f:
    generation, config, population, species_set, rndstate = pickle.load(f)
    print(population.best_genome)
    nn = neat.nn.FeedForwardNetwork.create(population.best_genome, config)
    #up = pickle.load(f)