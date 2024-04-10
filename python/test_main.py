from main import generate_initial_population, evolve_population


def test_population_keeps_same_size_after_one_iteration():
    # Given
    population_size = 12
    initial_population = generate_initial_population(population_size)

    # When
    new_population = evolve_population(1, initial_population, 'rank', mutation_rate=0.1)

    # Then
    assert len(new_population) == 12
