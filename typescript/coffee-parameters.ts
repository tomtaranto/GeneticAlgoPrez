export class CoffeeParameters {
    public score: number = 0

    public waterHardness: number
    public grainGrinding: number
    public waterTemperature: number
    public coffeeDose: number
    public tastingAltitude: number

    constructor(
        waterHardness: number,
        grainGrinding: number,
        waterTemperature: number,
        coffeeDose: number,
        tastingAltitude: number
    ) {
        this.waterHardness = waterHardness
        this.grainGrinding = grainGrinding
        this.waterTemperature = waterTemperature
        this.coffeeDose = coffeeDose
        this.tastingAltitude = tastingAltitude
    }

    static randomParameters(): CoffeeParameters {
        return new CoffeeParameters(
            Math.random() * 10,
            Math.random() * 10,
            Math.random() * 10,
            Math.random() * 10,
            Math.random() * 10
        )
    }
}