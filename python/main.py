from typing import List

import numpy as np

from coffee_parameters import CoffeeParameters
from constants import MIN_PARAMETER_VALUE, MAX_PARAMETER_VALUE
from evaluate import score


def generate_initial_population(n: int) -> List[CoffeeParameters]:
    return [CoffeeParameters.random_parameters() for _ in range(n)]


def evaluate_population(initial_population: List[CoffeeParameters]) -> List[float]:
    return [score(coffee_parameters) for coffee_parameters in initial_population]


def selection(population: List[CoffeeParameters], scores: List[float], function: str) -> List[CoffeeParameters]:
    sorted_population = [x for _, x in sorted(zip(scores, population), key=lambda pair: pair[0], reverse=True)]
    if function == 'rank':
        kept_individuals = sorted_population[:int(len(population) / 2)]
        return kept_individuals
    elif function == 'roulette':
        pass
    elif function == 'tournament':
        pass
    else:
        raise ValueError(f'Unknown selection function: {function}')


def crossover(parents: List[CoffeeParameters]) -> List[CoffeeParameters]:
    children = []
    for i in range(0, len(parents), 2):
        father, mother = parents[i], parents[i + 1]
        child1 = CoffeeParameters(
            water_hardness=(father.water_hardness + mother.water_hardness) / 2,
            grain_grinding=(father.grain_grinding + mother.grain_grinding) / 2,
            water_temperature=(father.water_temperature + mother.water_temperature) / 2,
            coffee_dose=(father.coffee_dose + mother.coffee_dose) / 2,
            tasting_altitude=(father.tasting_altitude + mother.tasting_altitude) / 2
        )
        child2 = CoffeeParameters(
            water_hardness=(father.water_hardness + mother.water_hardness) / 2,
            grain_grinding=(father.grain_grinding + mother.grain_grinding) / 2,
            water_temperature=(father.water_temperature + mother.water_temperature) / 2,
            coffee_dose=(father.coffee_dose + mother.coffee_dose) / 2,
            tasting_altitude=(father.tasting_altitude + mother.tasting_altitude) / 2
        )
        children.append(child1)
        children.append(child2)
    return children


def mutation(children: List[CoffeeParameters], mutation_rate: float = 0.1) -> List[CoffeeParameters]:
    generator = np.random.default_rng()
    for child in children:
        should_mutate = generator.random(5)
        if should_mutate[0] < mutation_rate:
            child.water_hardness = np.clip(child.water_hardness + generator.normal(-1, 1), MIN_PARAMETER_VALUE,
                                           MAX_PARAMETER_VALUE)
        if should_mutate[1] < mutation_rate:
            child.grain_grinding = np.clip(child.grain_grinding + generator.normal(-1, 1), MIN_PARAMETER_VALUE,
                                           MAX_PARAMETER_VALUE)
        if should_mutate[2] < mutation_rate:
            child.water_temperature = np.clip(child.water_temperature + generator.normal(-1, 1), MIN_PARAMETER_VALUE,
                                              MAX_PARAMETER_VALUE)
        if should_mutate[3] < mutation_rate:
            child.coffee_dose = np.clip(child.coffee_dose + generator.normal(-1, 1), MIN_PARAMETER_VALUE,
                                        MAX_PARAMETER_VALUE)
        if should_mutate[4] < mutation_rate:
            child.tasting_altitude = np.clip(child.tasting_altitude + generator.normal(-1, 1), MIN_PARAMETER_VALUE,
                                             MAX_PARAMETER_VALUE)
    return children


def replacement(parents: List[CoffeeParameters], children: List[CoffeeParameters]) -> List[CoffeeParameters]:
    return parents + children


def __log_best_parameters(population):
    best_coffee_parameters = max(population, key=lambda x: score(x))
    print(f'Best coffee can be made with the following parameters:'
          f'\nWater hardness: {best_coffee_parameters.water_hardness}'
          f'\nGrain grinding: {best_coffee_parameters.grain_grinding}'
          f'\nWater temperature: {best_coffee_parameters.water_temperature}'
          f'\nCoffee dose: {best_coffee_parameters.coffee_dose}'
          f'\nTasting altitude: {best_coffee_parameters.tasting_altitude}'
          f'\nScore: {score(best_coffee_parameters)}')


def validate_parameters(iteration, population_size, selection_function):
    if iteration < 1:
        raise ValueError('Iteration must be greater than 0')
    if population_size < 1:
        raise ValueError('Population size must be greater than 0')
    if population_size % 4 != 0:
        raise ValueError('Population size must be a multiple of 4')
    if selection_function not in ['rank', 'roulette', 'tournament']:
        raise ValueError('Unknown selection function')


def evolve_population(iteration, population, selection_function):
    scores = evaluate_population(population)
    print(f'Iteration {iteration}: {max(scores)}')
    parents = selection(population, scores, selection_function)
    children = crossover(parents)
    children = mutation(children, mutation_rate=0.1)
    population = replacement(parents, children)
    return population


def genetic_algo(iteration: int = 5, population_size: int = 100, selection_function: str = 'rank'):
    validate_parameters(iteration, population_size, selection_function)
    population: List[CoffeeParameters] = generate_initial_population(population_size)
    for iteration in range(iteration):
        population = evolve_population(iteration, population, selection_function)
    __log_best_parameters(population)


def main():
    genetic_algo(100, 120)


if __name__ == '__main__':
    main()
