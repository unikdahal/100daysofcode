import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


turtle.speed(0)


def draw_spirograph(size_of_graph):
    for i in range(int(360 / size_of_graph)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_graph)


draw_spirograph(1)

screen = Screen()
screen.exitonclick()
