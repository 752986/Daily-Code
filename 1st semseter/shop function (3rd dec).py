# pyright: strict

import random


def colored_text(text: str, color: int):
    return "\x1b[3{}m".format(color) + text + "\x1b[0m"


class Item:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class Player:
    inventory: list[Item]
    def __init__(self, money: int):
        self.money = money
        self.inventory = []

class Shop:
    def __init__(self):
        names: list[str] = [
    		"burger",
		    "pizza",
		    "glass bottle",
		    "magic stick",
		    "snake friend",
		    "health potion",
		    "cool glasses",
		    "a few coins",
		    "the color blue",
		    "cursed amulet",
		    "blessed amulet",
		    "glowing gemstone",
		    "hacking device",
		    "neat hat",
		]
        self.items: list[Item] = [Item(names.pop(random.randint(0, len(names) - 1)), random.randint(1, 30), random.randint(1, 15)) for _ in range(random.randint(5, 10))]

    def shop(self, player: Player, intro: bool = True) -> bool:
        print(colored_text("\n" + ("-" * 20), 0))
        if intro:
            print("welcome to my " + colored_text("shop", 5) + "! it looks like you have " + colored_text("{} coins".format(player.money), 3) + ". \n")

        print("what would you like to buy?")
        for item in self.items:
            if item.quantity > 0:
                print(colored_text("{}c ".format(item.price), 3) + item.name + colored_text(" ({})".format(item.quantity), 0))
        
        choice = input("> ").lower()
        if choice in ["exit", "quit"]:
            return True

        print()

        if choice in ["i", "inventory", "items"]:
            print("you have " + colored_text("{} coins", 3).format(player.money))
            for item in player.inventory:
                print(item.name + colored_text(" ({})".format(item.quantity), 0))
            return False


        item_to_buy: Item
        for item in self.items:
            if item.name == choice:
                if item.quantity > 0:
                    item_to_buy = item
                    break
                else:
                    print("sorry, i'm out of stock on that.")
                    return False
        else:
            print("sorry, i don't have that.")
            return False
        
        if item_to_buy.price > player.money:
            print("aww, you don't have enough money to buy that.")
            return False
        else:
            print(random.choice(["thanks for your purchase!", "enjoy your {}!".format(item_to_buy.name), "pleasure doing business with ya'!"]))
            player.money -= item_to_buy.price
            item_to_buy.quantity -= 1
            if item_to_buy.name == "a few coins":
                player.money += 2
            for item in player.inventory:
                if item.name == item_to_buy.name:
                    item.quantity += 1
                    break
            else:
                player.inventory.append(Item(item_to_buy.name, item_to_buy.price, 1))
        
        return False


if __name__ == "__main__":
	s = Shop()
	p = Player(random.randint(20, 100))
	
	print("\n(`i` to view your inventory, `exit` to quit)")
	first_run = True
	
	while True:
	    if s.shop(p, first_run): # will return true if the player wants to exit
	        break
	
	    first_run = False
