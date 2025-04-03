from turtle import Turtle,Screen
import random

COLORS = ["chartreuse4", "DarkSlateGray4","DarkSlateBlue","burlywood1","DarkOrchid4"]
screen = Screen()
# Challenge 2
def makeBrokenLines(turtle):
    for _ in range(0,10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

# Challenge 3   & somewhat # Challenge 1 
def draw_shape(turtle,num_side):
    turtle.color(random.choice(COLORS))
    for _ in range(num_side):
        angle = 360/num_side
        turtle.forward(100) 
        turtle.right(angle)
        
 # Challenge 4       
def draw_random(turtle):
    turtle.pensize(10)
    turtle.speed("fastest")
    DIRECTIONS = [0,90,180,270]
    for _ in range(500):
        random_Color(turtle)
       # turtle.color(random.choice(COLORS))
        steps = int(random.randint(-1,1)*30)
        angle = int(random.choice(DIRECTIONS))
        turtle.forward(steps)
        turtle.right(angle)
        
# Mini Challenge   -> Generate Random Colors with Tuple
def random_Color(turtle):
    screen.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r,g,b)
    turtle.color(new_color)

# Challenge 5 -> Spirograph
def make_spiro(turtle):
    turtle.speed("fastest")
    for _ in range(500):
        random_Color(turtle)
        turtle.circle(90)
        turtle.right(_)
    
    
timmy = Turtle()
timmy.shape("turtle")
# Challenge 5 - > Spirograph
make_spiro(timmy)

# Challenge 4 
# draw_random(timmy)
# Make timmy the turtle have multiple shapes
# for _ in range(3,10):
#     draw_shape(timmy,_)


screen.exitonclick()