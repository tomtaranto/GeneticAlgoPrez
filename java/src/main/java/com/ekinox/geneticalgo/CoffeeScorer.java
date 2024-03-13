package com.ekinox.geneticalgo;

import java.util.Comparator;
import java.util.List;

public class CoffeeScorer {
    public static double score(CoffeeParameters coffeeParameters) {
        double wh = coffeeParameters.waterHardness / 10.0;
        double gg = coffeeParameters.grainGrinding / 10.0;
        double wt = coffeeParameters.waterTemperature / 10.0;
        double cd = coffeeParameters.coffeeDose / 10.0;
        double ta = coffeeParameters.tastingAltitude / 10.0;

        double expComponent = Math.exp(-Math.abs(0.5 - (wh + wt) / 2) * Math.abs(0.5 - (wh + wt) / 2)) * Math.exp(-Math.pow(Math.abs(0.5 - gg), 1.5));

        double logComponent = Math.log1p(gg * cd * ta) / Math.log(2 + Math.abs(wh - wt) * Math.abs(wh - wt));

        double sinComponent = Math.sin(wt * Math.PI) * Math.cos(wh * Math.PI / 2);

        double tanhComponent = Math.tanh(wh + gg + wt + cd + ta);

        double conditionalComponent;
        if (wt > 0.5) {
            conditionalComponent = Math.log1p(Math.abs(wt - wh) + Math.abs(gg - cd));
        } else {
            conditionalComponent = Math.sin(ta * Math.PI);
        }

        double quadraticComponent = (wh - gg) * (wh - gg) + (wt - cd) * (wt - cd);

        double score = (expComponent * 1.5 + logComponent * 2 + sinComponent * 2.5 + tanhComponent * 3 +
                        conditionalComponent * 2 + quadraticComponent * 1.5) / 12;

        return (Math.round(score * 10 * 100.0) / 100.0); // Normalize score to range [0, 10] and round to 2 decimal places
    }


    public static CoffeeParameters findBestCoffeeParameters(List<CoffeeParameters> population) {
        return population.stream().max(Comparator.comparingDouble(p -> p.score)).orElse(null);
    }
}
