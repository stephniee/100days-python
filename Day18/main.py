from turtle import Turtle,Screen
from random import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    timmy.right(angle)
    timmy.fd(steps)













screen = Screen()
screen.exitonclick()