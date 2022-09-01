import random
import turtle


step = 10

def randf(start: float, stop: float):
    return random.random() * (stop - start) + start


screen = turtle.Screen()
screen.bgcolor(0.1, 0.1, 0.1)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen.tracer(100000)
color = [0.5, 0.5, 0.5]
t.color(color[0], color[1], color[2])
t.width(15)

count = 0
i = 0
negative = 0.02
while True:
    t.goto(t.pos() + turtle.Vec2D(randf(-step, step), randf(-step, step)))
    if abs(t.pos()[0]) > screen.window_width() / 2 or abs(t.pos()[1]) > screen.window_height() / 2:
        t.penup()
        t.goto(randf(-screen.window_width() / 2, screen.window_width() / 2), randf(-screen.window_height() / 2, screen.window_height() / 2))
        t.pendown()
    if count % 100 == 0:
        i = random.randint(0, 2)
    for c in t.color()[0]:
        if c > 254 / 255 or c < 1 / 255:
            negative *= -1
    color[i] += 1 / 255 * negative
    t.color(color[0], color[1], color[2])

    count += 1