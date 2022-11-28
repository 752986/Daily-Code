import os
import random


digits = "0123456789abcdef"


print("hit enter for new colors, type `quit` to exit")

i: str = ""
while i != "quit":
    i = input("> ")

    color = random.choice(digits)
    color += random.choice(digits)

    os.system("color " + color)

os.system("color 07")