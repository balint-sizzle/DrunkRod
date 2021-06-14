###
# input: angle
# output: movement
# fitness: time alive

from __future__ import print_function
import os
import neat
import visualize
from time import sleep
from rod_sim import Jack
from visualise_rod import RodDraw


sigmoid_scaling_factor = 100

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        jack = Jack()
        while jack.time_elapsed < 100 and not jack.fallen:
            angle = jack.get_angle()
            if abs(angle) > 45:
                jack.fallen = True
                break
            output = net.activate([angle])[-1]
            jack.move_base(output * sigmoid_scaling_factor)
        genome.fitness = jack.time_elapsed

def run(config):
    # Load configuration.
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                "config.ini")

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)
    print("Popoulation created")

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(4))
    print("Reporter created")

    # Run for up to 300 generations.
    print("Starting run")
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    jack_draw = RodDraw()
    while jack_draw.jack_rod.time_elapsed < 100 and not jack_draw.jack_rod.fallen:
        output = winner_net.activate([jack_draw.jack_rod.get_angle()])[-1]
        jack_draw.jack_rod.move_base(output * sigmoid_scaling_factor)
        jack_draw.draw()
    jack_draw.kill()

    # node_names = {-1:'angle', 0:'delta_p'}
    # visualize.draw_net(config, winner, True, node_names=node_names)
    # visualize.plot_stats(stats, ylog=False, view=True)
    # visualize.plot_species(stats, view=True)

    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    #p.run(eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)

