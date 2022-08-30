import random

class Fish:
    types = ["trout", "salmon", "carp", "tuna", "bass", "tilapia", "koi"]
    colors = ["brown", "blue", "red", "gray", "white", "orange"]

    def __init__(self, species: str = None, size: float = None, color: str = None, saltwater: bool = None):
        if None in [species, size, color, saltwater]:
            self.randomize()
        else:
            self.species = species
            self.size = size
            self.color = color
            self.saltwater = saltwater

    def randomize(self):
        self.species = random.choice(Fish.types)
        self.size = random.random() * 12
        self.color = random.choice(Fish.colors)
        self.saltwater = random.choice([True, False])

    def __str__(self):
        return "{}\" {} {} ({})".format(round(self.size, 2), self.color, self.species, "saltwater" if self.saltwater else "freshwater")


def search_fish(fishes: list[Fish]):
    # get user input:
    query = input("What would you like to search for? (`key: value` format, `all` for summary, `exit` to quit) \n> ").lower().replace(" ", "")
    if query in ["exit", "quit"]:
        return
    if query == "all":
        for f in fishes:
            print(f)
        print("\n({} fish in database)".format(len(fishes)))
        search_fish(fishes)
        return
    query_parts = query.split(":")
    if len(query_parts) != 2:
        print("Invalid query!")
        search_fish(fishes)
        return
    key = query_parts[0]
    value = query_parts[1]

    # check user input, to avoid code injection:
    if key in ["species", "type"]:
        key = "species"
        safe = value in Fish.types
    elif key == "color":
        safe = value in Fish.colors
    elif key in ["size", "length"]:
        key = "size"
        value = float(value)
        safe = True
    elif key == "saltwater":
        if value == "true":
            value = True
            safe = True
        elif value == "false":
            value = False
            safe = True
        else:
            safe = False
    else:
        safe = False

    if safe:
        results = 0
        for f in fishes:
            if key == "size":
                if abs(value - f.size) <= 0.5:
                    print(f)
            elif eval("f.{}".format(key)) == value:
                results += 1
                print(f)

        print("\n({} results found)".format(results))
        search_fish(fishes)
        return
    else:
        print("Invalid query!")
        search_fish(fishes)
        return


fishes = [Fish() for i in range(30)]

search_fish(fishes)