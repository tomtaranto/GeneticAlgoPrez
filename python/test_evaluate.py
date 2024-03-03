from evaluate import score
from coffee_parameters import CoffeeParameters


def test_score_returns_a_positive_float_for_0_values():
    cp = CoffeeParameters(water_hardness=0, grain_grinding=0, water_temperature=0, coffee_dose=0, tasting_altitude=0)
    print(score(cp))
    assert score(cp) > 0


def test_score_returns_a_positive_float_for_10_values():
    cp = CoffeeParameters(water_hardness=10, grain_grinding=10, water_temperature=10, coffee_dose=10,
                          tasting_altitude=10)
    print(score(cp))
    assert score(cp) > 0
