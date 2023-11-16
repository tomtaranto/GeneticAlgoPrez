MUTATION_RATE = 0.1
POPULATION_SIZE = 800
NEW_ELEMENTS_EACH_GENERATION = 10
GENERATIONS = 1001
SELECTION_FUNCTION = 'rank'
PLOT_BEST_EVERY = 10
PLOT_DIR = 'plots'
DATASET = "paris_metro"  # Available values: "random", "paris_metro"
NUMBER_OF_CITIES = 332 if DATASET == "paris_metro" else 50


if NEW_ELEMENTS_EACH_GENERATION % 2 != 0:
    raise ValueError(
        'NEW_ELEMENTS_EACh_GENERATION must be multiple of 2. Dealing with other population size is not implemented yet.')
if NEW_ELEMENTS_EACH_GENERATION > POPULATION_SIZE / 2:
    raise ValueError(
        'NEW_ELEMENTS_EACh_GENERATION must be smaller than POPULATION_SIZE/2. Dealing with other population size is not implemented yet.')
if POPULATION_SIZE % 4 != 0:
    raise ValueError(
        'Population size must be multiple of 4. Dealing with other population size is not implemented yet.')
if PLOT_BEST_EVERY > GENERATIONS:
    raise ValueError(f'PLOT_BEST_EVERY should be smaller than GENERATIONS. ')
