import csv

class Pokemon:
    level: int
    data: dict[str, str]

    def __init__(self, name: str, level: int):
        with open("pokemon.csv", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Name"].lower() == name.lower():
                    self.data = row
                    self.level = level
                    return
        raise NameError("Could not find a gen 1 pokemon with that name!")

class Move:
    power: int
    kind: str

    def __init__(self, power: int, kind: str) -> None:
        self.power = power
        self.kind = kind.capitalize()


def affinity(attacker: str, defender: str) -> float:
    with open("pokemon.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Attacking"].lower() == attacker.lower():
                return float(row[defender])
    raise NameError("Could not find the type!")

def damage(defender: Pokemon, attacker: Pokemon, move: Move):
    crit: bool = False

    return (((2 * attacker.level * (2 if crit else 1) + 2) * move.power * int(attacker.data["Attack"]) / int(defender.data["Defense"])) / 50 + 2) * (1.5 if move.kind == attacker.data["Type 1"] else 1)


Pokemon("Ivysaur", 10)