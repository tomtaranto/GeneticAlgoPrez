import java.util.Random;

public class CoffeeParameters {
    double waterHardness;
    double grainGrinding;
    double waterTemperature;
    double coffeeDose;
    double tastingAltitude;
    double score;

    public CoffeeParameters(double waterHardness, double grainGrinding, double waterTemperature, double coffeeDose, double tastingAltitude) {
        if (waterHardness < 0 || grainGrinding < 0 || waterTemperature < 0 || coffeeDose < 0 || tastingAltitude < 0) {
            throw new IllegalArgumentException("All parameters must be positive");
        }
        if (waterHardness > 10 || grainGrinding > 10 || waterTemperature > 10 || coffeeDose > 10 || tastingAltitude > 10) {
            throw new IllegalArgumentException("All parameters must be less than 10");
        }
        this.waterHardness = waterHardness;
        this.grainGrinding = grainGrinding;
        this.waterTemperature = waterTemperature;
        this.coffeeDose = coffeeDose;
        this.tastingAltitude = tastingAltitude;
        this.score= 0;
    }

    public CoffeeParameters() {
        Random rand = new Random();
        this.waterHardness = rand.nextDouble() * 10;
        this.grainGrinding = rand.nextDouble() * 10;
        this.waterTemperature = rand.nextDouble() * 10;
        this.coffeeDose = rand.nextDouble() * 10;
        this.tastingAltitude = rand.nextDouble() * 10;
        this.score = 0;
    }

    public void setScore(double score) {
        this.score = score;
    }

    public void setWaterHardness(double waterHardness) {
        this.waterHardness = waterHardness;
    }

    public void setGrainGrinding(double grainGrinding) {
        this.grainGrinding = grainGrinding;
    }

    public void setWaterTemperature(double waterTemperature) {
        this.waterTemperature = waterTemperature;
    }

    public void setCoffeeDose(double coffeeDose) {
        this.coffeeDose = coffeeDose;
    }

    public void setTastingAltitude(double tastingAltitude) {
        this.tastingAltitude = tastingAltitude;
    }
}
