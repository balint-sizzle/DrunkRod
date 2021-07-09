import gzip
import neat
import pickle
import visualize

with gzip.open("checkpoints/neat-checkpoint-"+"265") as f:
            generation, config, population, species_set, rndstate = pickle.load(f)
            print(population.best_genome)
            nn = neat.nn.FeedForwardNetwork.create(population.best_genome, config)

stats = population.reporters.reporters[1]
node_names = {-1:'angle', 0:'delta_p'}

visualize.draw_net(config, population.best_genome, True, node_names=node_names)
visualize.plot_stats(stats, ylog=False, view=True)
visualize.plot_species(stats, view=True)