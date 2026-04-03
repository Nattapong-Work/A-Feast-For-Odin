class FinalScore():

    @staticmethod
    def get_final_score(
            whale, knarr, long_ship, knarr_emi, long_emi, silver, income, occupation, shed, shed_minus,
            house, house_minus, longhouse, longhouse_minus, sheep, cattle, sheep_preg, cattle_preg,
            exploration_minus, village_minus
    ) -> int :
        score = (FinalScore.ship_score(whale, knarr, long_ship, knarr_emi, long_emi,) +
                 FinalScore.building_score(shed, house, longhouse) +
                 FinalScore.all_sum(silver, income, occupation) +
                 FinalScore.animal_score(sheep, cattle, sheep_preg, cattle_preg) -
                 FinalScore.all_min(shed_minus, house_minus, longhouse_minus,exploration_minus, village_minus))

        return score


    @staticmethod
    def all_sum(silver, income, occupation) -> int:
        score = (silver + income + occupation)
        print(f"all sum : {score}")
        return score

    @staticmethod
    def all_min(shed_minus, house_minus, longhouse_minus, exploration_minus, village_minus) -> int :
        score = (shed_minus + house_minus + longhouse_minus + exploration_minus + village_minus)
        print(f"all min : {score}")
        return score

    @staticmethod
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

    @staticmethod
    def exploration_score() -> int:
        pass

    @staticmethod
    def building_score(shed, house, long_house) -> int:
        score = (
            (shed * 8) +
            (house * 10) +
            (long_house * 17)
        )
        print(f"building : {score}")
        return score

    @staticmethod
    def animal_score(sheep, sheep_preg, cattle, cattle_preg) -> int:
        score = (
            sheep_preg +
            cattle_preg +
            (sheep * 2) +
            (cattle * 3)
        )
        print(f"animal : {score}")
        return score

