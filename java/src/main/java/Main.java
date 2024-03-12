import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    public static void genetic_algo(Integer iterations, Integer populationSize, String selectionFunction) {
        validateParameters(iterations, populationSize, selectionFunction);
        List<CoffeeParameters> population = generateInitialPopulation(populationSize);
        for (Integer iteration = 0; iteration < iterations; iteration++) {
            population = evolvePopulation(iteration, population, selectionFunction);
        }
        logBestParameters(population);
    }

    public static double clamp(double val) {
        double min = 0;
        double max = 10;
        return Math.max(min, Math.min(max, val));
    }

    public static double randomNumber() {
        return Math.random() * 2 - 1;
    }

    public static void logBestParameters(List<CoffeeParameters> population) {
        CoffeeParameters bestCoffeeParameters = CoffeeScorer.findBestCoffeeParameters(population);
        System.out.println("Best coffee can be made with the following parameters:"
                           + "\nWater hardness: " + bestCoffeeParameters.waterHardness
                           + "\nGrain grinding: " + bestCoffeeParameters.grainGrinding
                           + "\nWater temperature: " + bestCoffeeParameters.waterTemperature
                           + "\nCoffee dose: " + bestCoffeeParameters.coffeeDose
                           + "\nTasting altitude: " + bestCoffeeParameters.tastingAltitude
                           + "\nScore: " + CoffeeScorer.score(bestCoffeeParameters));
    }

    public static List<CoffeeParameters> evolvePopulation(Integer iteration, List<CoffeeParameters> population, String selectionFunction) {
        population.forEach(p -> p.setScore(CoffeeScorer.score(p)));
        System.out.println("Iteration " + iteration + ": " + population.stream().map(p -> p.score).max(Double::compare).orElse(0.0));
        List<CoffeeParameters> parents = selection(population, selectionFunction);
        List<CoffeeParameters> children = crossover(parents);
        List<CoffeeParameters> mutatedChildren = mutation(children, 0.1);
        population = replacement(parents, mutatedChildren);
        return population;
    }

    private static List<CoffeeParameters> replacement(List<CoffeeParameters> parents, List<CoffeeParameters> children) {
        return Stream.concat(parents.stream(), children.stream()).collect(Collectors.toList());
    }

    private static List<CoffeeParameters> mutation(List<CoffeeParameters> children, double mutation_rate) {
        children.forEach(child -> {
            if (Math.random() < mutation_rate) {
                child.setWaterHardness(clamp(child.waterHardness + randomNumber()));
            }
            if (Math.random() < mutation_rate) {
                child.setGrainGrinding(clamp(child.grainGrinding + randomNumber()));
            }
            if (Math.random() < mutation_rate) {
                child.setWaterTemperature(clamp(child.waterTemperature + randomNumber()));
            }
            if (Math.random() < mutation_rate) {
                child.setCoffeeDose(clamp(child.coffeeDose + randomNumber()));
            }
            if (Math.random() < mutation_rate) {
                child.setTastingAltitude(clamp(child.tastingAltitude + randomNumber()));
            }
        });
        return children;
    }

    private static List<CoffeeParameters> crossover(List<CoffeeParameters> parents) {
        List<CoffeeParameters> children = new ArrayList<>();
        for (int i = 0; i < parents.size(); i += 2) {
            CoffeeParameters parent1 = parents.get(i);
            CoffeeParameters parent2 = parents.get(i + 1);
            CoffeeParameters child1 = new CoffeeParameters(
                    (parent1.waterHardness + parent2.waterHardness) / 2,
                    (parent1.grainGrinding + parent2.grainGrinding) / 2,
                    (parent1.waterTemperature + parent2.waterTemperature) / 2,
                    (parent1.coffeeDose + parent2.coffeeDose) / 2,
                    (parent1.tastingAltitude + parent2.tastingAltitude) / 2
            );
            CoffeeParameters child2 = new CoffeeParameters(
                    (parent1.waterHardness * 0.7 + parent2.waterHardness * 0.3),
                    (parent1.grainGrinding * 0.7 + parent2.grainGrinding * 0.3),
                    (parent1.waterTemperature * 0.7 + parent2.waterTemperature * 0.3),
                    (parent1.coffeeDose * 0.7 + parent2.coffeeDose * 0.3),
                    (parent1.tastingAltitude * 0.7 + parent2.tastingAltitude * 0.3)
            );
            children.addAll(Arrays.asList(child1, child2));
        }
        return children;
    }

    private static List<CoffeeParameters> selection(List<CoffeeParameters> population, String selectionFunction) {
        List<CoffeeParameters> orderedPopulation = population.stream()
                .sorted((p1, p2) -> Double.compare(p2.score, p1.score))
                .collect(Collectors.toList());
        switch (selectionFunction) {
            case "rank":
                return orderedPopulation.stream().limit(population.size() / 2).collect(Collectors.toList());
            case "roulette":
                throw new UnsupportedOperationException("Not implemented yet");
            case "tournament":
                throw new UnsupportedOperationException("Not implemented yet");
            default:
                throw new UnsupportedOperationException("Not implemented yet");
        }
    }

    public static List<CoffeeParameters> generateInitialPopulation(Integer populationSize) {
        return IntStream.range(0, populationSize)
                .mapToObj(i -> new CoffeeParameters())
                .collect(Collectors.toList());
    }

    private static void validateParameters(Integer iterations, Integer populationSize, String slectionFunction) {
        if (iterations < 1) {
            throw new IllegalArgumentException("Iterations must be greater than 0");
        }
        if (populationSize < 1) {
            throw new IllegalArgumentException("Population size must be greater than 0");
        }
        if (populationSize % 4 != 0) {
            throw new IllegalArgumentException("Population size must be a multiple of 4");
        }
        if (!slectionFunction.equals("rank") && !slectionFunction.equals("roulette") && !slectionFunction.equals("tournament")) {
            throw new IllegalArgumentException("Selection function must be 'rank' or 'roulette' or 'tournament'");
        }
    }

    public static void main(String[] args) {
        genetic_algo(100, 120, "rank");
    }
}
