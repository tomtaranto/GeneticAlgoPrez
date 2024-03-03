import math

from coffee_parameters import CoffeeParameters


def score(coffee_parameters: CoffeeParameters) -> float:
    # Extract parameters and normalize
    wh = coffee_parameters.water_hardness / 10.
    gg = coffee_parameters.grain_grinding / 10.
    wt = coffee_parameters.water_temperature / 10.
    cd = coffee_parameters.coffee_dose / 10.
    ta = coffee_parameters.tasting_altitude / 10.

    # Introduce more complex interactions
    exp_component = math.exp(-abs(0.5 - (wh + wt) / 2) ** 2) * math.exp(-abs(0.5 - gg) ** 1.5)

    log_component = math.log1p(gg * cd * ta) / math.log(2 + abs(wh - wt) ** 2)

    sin_component = math.sin(wt * math.pi) * math.cos(wh * math.pi / 2)

    tanh_component = math.tanh(wh + gg + wt + cd + ta)

    # Non-linear interaction with a conditional
    if wt > 0.5:
        conditional_component = math.log1p(abs(wt - wh) + abs(gg - cd))
    else:
        conditional_component = math.sin(ta * math.pi)

    # Quadratic interaction
    quadratic_component = (wh - gg) ** 2 + (wt - cd) ** 2

    # Mix components with varying weights
    score = (exp_component * 1.5 + log_component * 2 + sin_component * 2.5 + tanh_component * 3 +
             conditional_component * 2 + quadratic_component * 1.5) / 12

    # Normalize score to range [0, 10]
    return round(score * 10, 2)

