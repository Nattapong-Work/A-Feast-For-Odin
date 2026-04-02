def get_final_score() -> int :
    final_score = all_sum() - all_min()
    return final_score

def all_sum() -> int:
    final_score = (
        ship_score() +
        exploration_score() +
        building_score() +
        animal_score()
    )
    return final_score

def all_min() -> int :
    pass

def ship_score(whale, knarr, long_ship) -> int:
    final_score = (
        (whale * 3) +
        (knarr * 5) +
        (long_ship * 8)
    )
    return final_score

def exploration_score() -> int:
    pass

def building_score(shed, house, long_house) -> int:
    final_score = (
        (shed * 8) +
        (house * 10) +
        (long_house * 17)
    )
    return final_score

def animal_score(sheep, sheep_preg, cattle, cattle_preg) -> int:
    final_score = (
        sheep_preg +
        cattle_preg +
        (sheep * 2) +
        (cattle * 3)
    )
    return final_score

