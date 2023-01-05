import os
import random
import time


digits = "0123456789abcdef"


N_TIMES = 3

times: list[float] = []
for _ in range(N_TIMES):
    times.append(random.random())


print("hit enter for new colors, type `quit` to exit")

userin: str = ""
index = 0
while userin != "quit":
    # i = input("> ")
    time.sleep(times[index])
    index += 1
    index %= N_TIMES

    color = random.choice(digits)
    color += random.choice(digits)

    os.system("color " + color)

os.system("color 07")