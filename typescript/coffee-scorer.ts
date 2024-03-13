import {CoffeeParameters} from "./coffee-parameters";

export class CoffeeScorer {
    public static score(coffeeParameters: CoffeeParameters): number {
        const wh = coffeeParameters.waterHardness / 10.0;
        const gg = coffeeParameters.grainGrinding / 10.0;
        const wt = coffeeParameters.waterTemperature / 10.0;
        const cd = coffeeParameters.coffeeDose / 10.0;
        const ta = coffeeParameters.tastingAltitude / 10.0;

        const expComponent = Math.exp(-(Math.abs(0.5 - (wh + wt) / 2) ** 2)) * Math.exp(-(Math.abs(0.5 - gg) ** 1.5));

        const logComponent = Math.log1p(gg * cd * ta) / Math.log(2 + Math.abs(wh - wt) ** 2);

        const sinComponent = Math.sin(wt * Math.PI) * Math.cos(wh * Math.PI / 2);

        const tanhComponent = Math.tanh(wh + gg + wt + cd + ta);

        let conditionalComponent: number;
        if (wt > 0.5) {
            conditionalComponent = Math.log1p(Math.abs(wt - wh) + Math.abs(gg - cd));
        } else {
            conditionalComponent = Math.sin(ta * Math.PI);
        }

        const quadraticComponent = (wh - gg) ** 2 + (wt - cd) ** 2;

        const score = (expComponent * 1.5 + logComponent * 2 + sinComponent * 2.5 + tanhComponent * 3 +
            conditionalComponent * 2 + quadraticComponent * 1.5) / 12;

        return Math.round(score * 10 * 100.0) / 100.0; // Normalize score to range [0, 10] and round to 2 decimal places
    }

    public static findBestCoffeeParameters(population: CoffeeParameters[]): CoffeeParameters | null {
        return population.sort((a, b) => this.score(b) - this.score(a))[0] || null;
    }
}