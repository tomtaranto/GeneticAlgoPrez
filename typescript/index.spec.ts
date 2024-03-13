import {evolvePopulation, generatePopulation} from "./index";

describe('evolve', () => {
    it('should not change the population size', () => {
        // Given
        const populationSize = 12
        const initialPopulation = generatePopulation(populationSize)

        // When
        const evolvedPopulation = evolvePopulation(0, initialPopulation, 'rank')

        // Then
        expect(evolvedPopulation.length).toBe(populationSize)
    })
})