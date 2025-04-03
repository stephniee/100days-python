import colorgram
from turtle import Screen, Turtle 
import random 

timmy = Turtle()
screen = Screen()

IMAGE = 'mona-lisa.jpg'

def get_color():
    colors = colorgram.extract(IMAGE,50)
    color_list = [tuple(color.rgb) for color in colors]
    return color_list

def assign_color(num,color):
    screen.colormode(255)
    if num < len(color):
        r, g, b = color[num]
        color_list = (r,g,b)
        return color_list
    
def make_dots(turtle):
    size = 20
   
    for _ in range(10):  # 10 rows of dots
        for _ in range(10):  # 10 dots per row
            random_number = random.randint(0,(len(color_list)-1))
            color = assign_color(random_number, color_list)
            turtle.dot(size, color)
            turtle.forward(50)  
            
        turtle.setheading(90)  
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)  

    
timmy.penup()
timmy.setheading(210)
timmy.forward(300)
timmy.setheading(0)        
color_list = get_color() 
make_dots(timmy)
    
screen.exitonclick()  
    