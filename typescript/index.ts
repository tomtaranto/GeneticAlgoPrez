import {CoffeeParameters} from "./coffee-parameters";
import {CoffeeScorer} from "./coffee-scorer";

function validateParameters(iterations: number, populationSize: number, selection_function: string) {
    if (iterations < 1) {
        throw new Error('Iterations must be a positive number')
    }
    if (populationSize < 1) {
        throw new Error('Population size must be a positive number')
    }
    if (populationSize % 4 != 0) {
        throw new Error('Population size must be divisible by 4')
    }
    if (selection_function !== 'rank' && selection_function !== 'roulette' && selection_function !== 'tournament') {
        throw new Error('Selection function must be either rank or roulette')
    }
}

export function generatePopulation(populationSize: number): CoffeeParameters[] {
    let population: CoffeeParameters[] = []
    for (let i = 0; i < populationSize; i++) {
        population.push(CoffeeParameters.randomParameters())
    }
    return population
}

function evaluatePopulation(population: CoffeeParameters[]) {
    population.map((coffeeParameters) => {
        coffeeParameters.score = CoffeeScorer.score(coffeeParameters)
    });
}

function selection(population: CoffeeParameters[], selection_function: string) {
    const sortedPopulation = population.sort((a, b) => b.score - a.score)
    if (selection_function === 'rank') {
        return sortedPopulation.slice(0, sortedPopulation.length / 2)
    } else if (selection_function === 'roulette') {
        throw new Error("not implemented")
    } else if (selection_function === 'tournament') {
        throw new Error("not implemented")
    } else {
        throw new Error("Invalid selection function")
    }
}

function crossover(parents: CoffeeParameters[]) {
    const children: CoffeeParameters[] = []
    for (let i = 0; i < parents.length; i += 2) {
        const parent1 = parents[i]
        const parent2 = parents[i + 1]
        const child1 = new CoffeeParameters(
            (parent1.waterHardness + parent2.waterHardness) / 2,
            (parent1.grainGrinding + parent2.grainGrinding) / 2,
            (parent1.waterTemperature + parent2.waterTemperature) / 2,
            (parent1.coffeeDose + parent2.coffeeDose) / 2,
            (parent1.tastingAltitude + parent2.tastingAltitude) / 2
        )
        const child2 = new CoffeeParameters(
            (parent1.waterHardness * 0.7 + parent2.waterHardness * 0.3),
            (parent1.grainGrinding * 0.7 + parent2.grainGrinding * 0.3),
            (parent1.waterTemperature * 0.7 + parent2.waterTemperature * 0.3),
            (parent1.coffeeDose * 0.7 + parent2.coffeeDose * 0.3),
            (parent1.tastingAltitude * 0.7 + parent2.tastingAltitude * 0.3)
        )
        children.push(child1)
        children.push(child2)
    }
    return children
}

function clamp(value: number): number {
    return Math.max(10, Math.min(0, value))
}

function mutation(children: CoffeeParameters[]) {
    children.forEach((child) => {
        if (Math.random() < 0.1) {
            child.waterHardness = clamp(child.waterHardness + Math.random() * 2 - 1)
        }
        if (Math.random() < 0.1) {
            child.grainGrinding = clamp(child.grainGrinding + Math.random() * 2 - 1)
        }
        if (Math.random() < 0.1) {
            child.waterTemperature = clamp(child.waterTemperature + Math.random() * 2 - 1)
        }
        if (Math.random() < 0.1) {
            child.coffeeDose = clamp(child.coffeeDose + Math.random() * 2 - 1)
        }
        if (Math.random() < 0.1) {
            child.tastingAltitude = clamp(child.tastingAltitude + Math.random() * 2 - 1)
        }
    })
    return children
}

function replacement(population: CoffeeParameters[], mutatedChildren: CoffeeParameters[]) {
    return population.concat(mutatedChildren)
}

export function evolvePopulation(iteration: number, population: CoffeeParameters[], selection_function: string): CoffeeParameters[] {
    evaluatePopulation(population)
    console.log(`Iteration ${iteration} : ${CoffeeScorer.findBestCoffeeParameters(population)?.score}`);
    const parents = selection(population, selection_function)
    const children = crossover(parents)
    const mutatedChildren = mutation(children)
    return replacement(parents, mutatedChildren)
}

function geneticAlgo(iterations: number = 5, populationSize: number = 100, selection_function: string = 'rank') {
    validateParameters(iterations, populationSize, selection_function)
    let population: CoffeeParameters[] = generatePopulation(populationSize)
    for (let iteration = 0; iteration < iterations; iteration++) {
        population = evolvePopulation(iteration, population, selection_function)
    }

}

function main() {
    geneticAlgo(100, 120)
}


main()