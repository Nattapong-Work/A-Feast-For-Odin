score = {
         "sheep" : 2,
         "cattle" : 3,
         }


pregnant = 1
english_crown = 2
occupation = 0
silver = 0
income = 0
sheep = 0
cattle = 0
shed = 0
house = 0
longhouse = 0

max_whale = 3
max_knarr_longship = 3

total_score = 0


def ship_score() -> int: # *********** นับคะแนน แต่ยังไม่ได้ทำ error handle เช่นจำนวนติดลบ หรือตัวอักษร ***********
    ship_values = {
        "Whaling Ship": 3,
        "Knarr": 5,
        "Longship": 8,
        "Knarr Emigration": 18,
        "Longship Emigration": 21
    }

    total = 0
    for ship, value in ship_values.items():
        count = int(input(f"How many {ship} you have? : "))
        total += count * value
    print(f"Total ship score : ", total)
    print()
    return total

def exploration_score() -> int: # *********** นับคะแนน แต่ยังไม่ได้ทำ error handle เช่นจำนวนติดลบ หรือตัวอักษร ********************
    exploration = {"baffin": {"score": 12, "minus": 24},
                   "bare": {"score": 12, "minus": 22},
                   "faroe": {"score": 4, "minus": 16},
                   "greenland": {"score": 12, "minus": 20},
                   "iceland": {"score": 16, "minus": 24},
                   "labrador": {"score": 36, "minus": 40},
                   "newfoundland": {"score": 38, "minus": 40},
                   "shetland": {"score": 6, "minus": 24},
                   }

    total = 0
    for ise, value in exploration.items():
        island = input(f"Do you have {ise}? (y/n) : ") # **************** ต้องมาแฮฯเดิล แอเรอร์ อีก ************************
        if island == "y":
            final_minus = int(input(f"How many -1 on your {ise}? : "))
            if final_minus > value["minus"]:
                print("no no") # *********************************** ต้องแก้ ให้วนลูปรับค่าใหม่ เพราะตนอนี้มันข้ามไปเลย *************
            else:
                total += value["score"] - final_minus



    print(f"Total exploration score : ", total)
    print()
    return total

def building_score() -> int:
    house = {
        "shed": {"score": 8, "minus": 6},
        "house": {"score": 10, "minus": 9},
        "longhouse": {"score": 17, "minus": 15}
        }
    total = 0
    type_score = 0
    for build, value in house.items():
        building = input(f"Do you have {build}? (y/n) : ")
        if building == "y":
            type_score = 0
            building_count = int(input(f"How many {build} you have? : "))
            for i in range(building_count): # วนซ้ำตามจำนวนสิ่งก่อสร้างทีมี
                building_minus = int(input(f"How many -1 on your {build}? : "))
                if building_minus > value["minus"]:
                    print("no no") # ******************************** ต้องแก้ ให้วนลูปรับค่าใหม่ เพราะตนอนี้มันข้ามไปเลย *************
                else:
                    type_score += value["score"] - building_minus
                    total += value["score"] - building_minus
                    print()

            print(f"Your {build} score : ", type_score)
        print(f"Total building score : ", total)
    print()
    return total



def main():
    total_score = ship_score() + exploration_score() + building_score()
    print("Total score : ", total_score)


if __name__ == "__main__":
    main()
