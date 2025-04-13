from turtle import Turtle,Screen
import random



class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#000300")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.screen = Screen()
        self.refresh()
    
    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)