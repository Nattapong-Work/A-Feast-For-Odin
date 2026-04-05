
def get_final_score(
        whale, knarr, long_ship, knarr_emi, long_emi, silver, income, occupation, shed, shed_minus,
        house, house_minus, longhouse, longhouse_minus, sheep, cattle, sheep_preg, cattle_preg,
        exploration_minus, village_minus
) -> int :
    score = (ship_score(whale, knarr, long_ship, knarr_emi, long_emi,) +
             building_score(shed, house, longhouse) +
             all_sum(silver, income, occupation) +
             animal_score(sheep, cattle, sheep_preg, cattle_preg) +
             checkbox_point -
             all_min(shed_minus, house_minus, longhouse_minus,exploration_minus, village_minus)
)

    return score


def all_sum(silver, income, occupation) -> int:
    score = (silver + income + occupation)
    print(f"all sum : {score}")
    return score


def all_min(shed_minus, house_minus, longhouse_minus, exploration_minus, village_minus) -> int :
    score = (shed_minus + house_minus + longhouse_minus + exploration_minus + village_minus)
    print(f"all min : {score}")
    return score


def ship_score(whale, knarr, long_ship, knarr_emi, long_emi,) -> int:
    score = (
        (whale * 3) +
        (knarr * 5) +
        (long_ship * 8) +
        (knarr_emi * 18) +
        (long_emi * 21)
    )

    print(f"ship : {score}")
    return score


def building_score(shed, house, long_house) -> int:
    score = (
        (shed * 8) +
        (house * 10) +
        (long_house * 17)
    )
    print(f"building : {score}")
    return score


def animal_score(sheep, sheep_preg, cattle, cattle_preg) -> int:
    score = (
        sheep_preg +
        cattle_preg +
        (sheep * 2) +
        (cattle * 3)
    )
    print(f"animal : {score}")
    return score

data = {
    "Faroe Island" : 4,
    "Shetland" : 6,
    "Bear Island" : 12,
    "Baffin Island" : 12,
    "Greenland" : 12,
    "Iceland" : 16,
    "Labrador" : 36,
    "Newfoundland" : 38,
    "English Crown" : 2
}

checkbox_point = 0

def add_point(ise):
    if ise in data:
        global checkbox_point
        checkbox_point += data[ise]
        print(checkbox_point)

def sub_point(ise):
    if ise in data:
        global checkbox_point
        checkbox_point -= data[ise]
        print(checkbox_point)







