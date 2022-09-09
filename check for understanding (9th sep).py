import random

######

for i in range(3, 33, 5):
    print(i)

print() 
######

for i in range(100, 50, -2):
    print(i)

print() 
######

while True:
    num = float(input("enter a number: \n> "))
    if num == 0:
        break
    else:
        print(num * 2)

print() 
######

def monsterspawner():
    r = random.random()
    if r > 0.6:
        print("spiader")
    elif r > 0.3:
        print("skeleton")
    elif r > 0.1:
        print("zombie")
    else:
        print("witch")

for i in range(10):
    monsterspawner()

######

def average(a, b):
    print((a + b) / 2)

a = float(input("first number: \n> "))
b = float(input("second number: \n> "))
average(a, b)