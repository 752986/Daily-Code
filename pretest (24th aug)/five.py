import random
import turtle

def rand_color():
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    string = "#"
    for i in range(6):
        string += random.choice(chars)
    return string

class Ant:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

        self.queen = False

        self.color = rand_color()

        self.t = turtle.Turtle()
        self.t.color(self.color)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

    def report(self):
        print("coords: ({}, {}) \nqueen: {} \ncolor: {}".format(self.x, self.y, self.queen, self.color))

    def bark(self):
        print("woof")

    def march(self):
        self.x += (random.random() - 0.5) * 10
        self.y += (random.random() - 0.5) * 10

        self.t.goto(self.x, self.y)

# setup:
ants = [Ant() for i in range(3)]

# process loop:
while True:
    if random.random() > 0.01:
        for a in ants:
            a.report()
    
    for a in ants:
        if random.random() > 0.01:
            a.bark()
        
        if random.random() > 0.5:
            a.march()