import numpy as np
from pydantic import BaseModel, Field


class CoffeeParameters(BaseModel):
    water_hardness: float = Field(ge=0, le=10)  # Durete de l'eau
    grain_grinding: float = Field(ge=0, le=10)  # Mouture du grain
    water_temperature: float = Field(ge=0, le=10)  # Temperature de l'eau
    coffee_dose: float = Field(ge=0, le=10)  # Dose de cafe
    tasting_altitude: float = Field(ge=0, le=10)  # Altitude de degustation

    @classmethod
    def random_parameters(cls):
        generator = np.random.default_rng()
        random_parameters: np.ndarray = generator.random(5) * 10
        return cls(
            water_hardness=random_parameters[0],
            grain_grinding=random_parameters[1],
            water_temperature=random_parameters[2],
            coffee_dose=random_parameters[3],
            tasting_altitude=random_parameters[4]
        )
