from turtle import Screen 
import time
from Snake import Snake

# Screensetup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgpic("Day20/assets/nokia.png")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
# def tap_to_change():
#     screen.bgcolor("#8ab565")
 
  
# Keystroke Listener

game_is_on = True
# if screen.onkey(tap_to_change,"space"):
#     game_is_on = True

# else:
#     game_is_on = False

while game_is_on:
    screen.update()
    snake_body = Snake()
 
    time.sleep(.1)
    #Call Snake

   
    screen.onkey(snake_body.up,"Up")
    screen.onkey(snake_body.down,"Down")
    screen.onkey(snake_body.left,"Left")
    screen.onkey(snake_body.right,"Right")
    snake_body.follow()
 
        

screen.exitonclick()