import random
width = 10
height = 10
def print_rooms():
    for x in range (width):
        for y in range (height):
            print (rooms [x][y], end= " ")
        print ()
rooms: list[list[int]] = [[0 for _ in range(height)] for _ in range(width)]
x = random.randint(0,width-1)
y = random.randint(0,height-1)
rooms[x][y] = 1
for i in range(10):
    while True:
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        if x == 0 or y == 0 or x == width-1 or y == height-1: continue
        if rooms [x] [y] != 0: continue 
        if rooms[x+1][y] or rooms[x][y+1] or rooms[x-1][y] or rooms[x][y-1]:
            rooms[x][y] = random.randint(2,5)
            break
print_rooms()