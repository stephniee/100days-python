from turtle import Screen 
import time
from Snake import Snake

# Screensetup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("#8ab565")
screen.title("My Snake Game")
screen.tracer(0)



# Call Snake
snake_body = Snake()
game_is_on = True

# Keystroke Listener
screen.listen()
screen.onkey(snake_body.up,"w")
screen.onkey(snake_body.down,"s")
screen.onkey(snake_body.left,"a")
screen.onkey(snake_body.right,"d")



while game_is_on:
    screen.update()
    
    time.sleep(.1)
    
    snake_body.follow()
 
        

screen.exitonclick()