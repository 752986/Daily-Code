import csv
import random
import time

class Pokemon:
    '''Stores data imported from the `pokemon.csv` file'''

    level: int
    hp: int
    data: dict[str, str]

    def __init__(self, name: str, level: int):
        # find the correct pokemon in `pokemon.csv`
        with open("pokemon.csv", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Name"].lower() == name.lower():
                    self.data = row
                    self.level = level
                    self.hp = int((((float(row["HP"]) + random.randint(0, 15)) * 2 + 10) * self.level) / 100) + level + 10
                    return
            raise NameError("Could not find a gen 1 pokemon with that name!")

class Move:
    '''Stores data about a battle move'''

    name: str
    power: int
    kind: str

    def __init__(self):
        with open("pokemoves.csv", newline="") as file:
            # read a random move from `pokemoves.csv`
            reader = csv.DictReader(file)

            # choose a random index to pull from
            n_lines = 166
            chosen_move: int = random.randint(0, n_lines - 2)

            # go to that index and fill the instance's fields
            rows_seen = 0
            for row in reader:
                if rows_seen == chosen_move:
                    self.name = row["Name"]
                    self.power = int(row["Power"])
                    self.kind = row["Type"]
                    return
                rows_seen += 1
            raise IndexError("uh oh...")
                

def affinity(attacker: str, defender: str) -> float:
    '''Finds the type-based attack multiplier for the given attacking and defending types'''

    if attacker == "" or defender == "":
        return 1.0

    with open("poketypes.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Attacking"].lower() == attacker.lower():
                return float(row[defender])
        raise NameError("Could not find the attacking type!")

def damage(defender: Pokemon, attacker: Pokemon, move: Move) -> int:
    '''Finds the damage that `defender` takes when `attacker` attacks it with `move`'''

    if move.power == 0:
        return 0 

    # decide whether a crit happened
    crit: bool = random.random() < float(attacker.data["Speed"]) / (255 * 2)

    # calculate the type-based multiplier and print a message based on it
    overall_affinity = affinity(move.kind, defender.data["Type 1"]) * affinity(move.kind, defender.data["Type 2"])

    match overall_affinity:
        case 0:
            print("The move failed to land!")
        case 2:
            print("The move was super effective!")
        case _:
            pass

    if crit:
        print("A critical hit!")

    # calculate the damage that was done
    result = (((2 * attacker.level * (2 if crit else 1) + 2) * move.power * int(attacker.data["Attack"]) / int(defender.data["Defense"])) / 50 + 2) * (1.5 if move.kind in [attacker.data["Type 1"], attacker.data["Type 2"]] else 1) * overall_affinity * random.uniform(0.85, 1.0)

    return int(result)


def main():
    print("Choose two pokemon to battle!")

    # uncomment the following two lines to manually input the info instead
    #p1 = Pokemon(input("first pokemon's name: "), int(input("first pokemon's level: ")))
    #p2 = Pokemon(input("second pokemon's name: "), int(input("second pokemon's level: ")))
    p1 = Pokemon("pikachu", 20)
    p2 = Pokemon("eevee", 25)

    print("======\n")

    while p1.hp > 0 and p2.hp > 0:
        # reject moves that are likely too powerful for the level
        # roughly based on a linear regression of pikachu, bulbasaur, and charmander's movesets
        move1 = Move()
        while move1.power > 2 * p1.level + 20 or move1.power < 1:
            move1 = Move()

        move2 = Move()
        while move2.power > 2 * p2.level + 20 or move2.power < 1:
            move2 = Move()

        # pokemon 1 attacks
        print(f"{p1.data['Name']} used {move1.name}!")
        dmg = damage(p2, p1, move1)
        print(f"-{dmg} HP")
        p2.hp -= dmg
        print(f"{p1.data['Name']}'s HP: {max(p1.hp, 0)}")
        print(f"{p2.data['Name']}'s HP: {max(p2.hp, 0)}")

        time.sleep(1)

        # exit if one of the pokemon has fainted
        if p1.hp <= 0 or p2.hp <= 0:
            print()
            break

        print()

        # pokemon 2 attacks
        print(f"{p2.data['Name']} used {move2.name}!")
        dmg = damage(p2, p1, move1)
        print(f"-{dmg} HP")
        p1.hp -= dmg
        print(f"{p1.data['Name']}'s HP: {max(p1.hp, 0)}")
        print(f"{p2.data['Name']}'s HP: {max(p2.hp, 0)}")

        time.sleep(1)

        # exit if one of the pokemon has fainted
        if p1.hp <= 0 or p2.hp <= 0:
            print()
            break

        print("\n------\n")

    print("======")
    print("The battle is won!")

if __name__ == "__main__":
    main()