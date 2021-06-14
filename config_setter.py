import configparser

config = configparser.ConfigParser()

config["NEAT"] = {
    "fitness_criterion":"max",
    "fitness_threshold":0.5,
    "no_fitness_termination":False,
    "pop_size":2,
    "reset_on_extinction":False  # THIS WILL CAUSE AN EXCEPTION
}

config["DeaultStagnation"] = {
    "species_fitness_func":"max",
    "max_stagnation": 10, # species will be considered stagnant after 10 gens
    "species_elitism": 2 # 2 species will be kept to prevent total extinction
}

config["DefaultReproduction"] = {
    "elitism": 0,
    "survival_threshold": 0.2, # fraction of species allowed to reproduce
    "min_species_size": 2 # min nr genomes per species after reproduction
}

config["DefaultGenome"] = {
    "activation_default": "random",
    "activation_mutate_rate": 0.5,
    "aggregation_mutate_rate": 0.5,
    
    "bias_init_mean": 0.5,
    "bias_init_stdev": 0.2,
    "bias_max_value": 100,
    "bias_min_value": -100,
    "bias_mutate_power": 0.2,
    "bias_mutate_rate": 0.4,
    "bias_replace_rate": 0.4,

    "compatibility_threshold": 0.6,
    "compatibility_disjoint_coefficient": 0.5,
    "compatibility_weight_coefficient": 0.5,
    
    "enabled_default": True,
    "enabled_mutate_rate": 0.1,
    "enabled_rate_to_false_add": 0.2,
    "enabled_rate_to_true_add": 0.2,
    

    "feed_forward": True,

    "conn_add_prob": 0.2,
    "conn_delete_prob": 0.1,
    "node_add_prob": 0.3,
    "node_delete_prob": 0.1,
    
    "num_inputs": 1,
    "num_outputs": 1,
    "num_hidden": 1,
    
    "response_init_mean": 0.5,
    "response_init_stdev": 0.2,
    "response_max_value": 1,
    "response_min_value": -1,
    "response_mutate_power": 0.2,
    "response_mutate_rate": 0.4,
    "response_replace_rate": 0.4,
    
    "weight_init_mean": 0.5,
    "weight_init_stdev": 0.2,
    "weight_max_value": 1,
    "weight_min_value": -1,
    "weight_mutate_power": 0.2,
    "weight_mutate_rate": 0.4,
    "weight_replace_rate": 0.4,

}

with open("./config.ini", "w") as f:
    config.write(f)