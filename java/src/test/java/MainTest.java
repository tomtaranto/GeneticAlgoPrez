import com.ekinox.geneticalgo.CoffeeParameters;
import com.ekinox.geneticalgo.Main;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;


class MainTest {

    @Test
    public void evolvePopulationShouldKeepTheSameSizeAfterIterating() {
        // Given
        Integer population_size = 12;
        List<CoffeeParameters> population = Main.generateInitialPopulation(population_size);

        // When
        List<CoffeeParameters> evolvedPopulation = Main.evolvePopulation(0, population, "rank", 0.1);

        // Then
        assertEquals((long) population_size, (long) evolvedPopulation.size());
    }
}