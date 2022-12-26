import turtle
from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()
timmy_turtle.shape("arrow")
timmy_turtle.color("black")
timmy_turtle.speed(20)
turtle.colormode(255)
current_heading = timmy_turtle.heading()


def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def size_of_gap(no):
    for _ in range(int(360 / no)):
        timmy_turtle.color(rgb_color())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + no)


size_of_gap(5)
my_screen = Screen()
my_screen.exitonclick()
