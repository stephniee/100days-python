from turtle import Screen 
import time
from Snake import Snake
from Food import Food
from Score import Scoreboard, Lives
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#99C202")
screen.bgpic("Day20/assets/snake.gif")
screen.title("My Snake Game")
screen.tracer(0)
 

game_is_on = False
snake = None
food = None
scorer = None
life = None
 

def run_game_loop():
    while game_is_on:
        screen.update()
        
        time.sleep(0.1)
        
        screen.listen()
        # One-time key bindings and setup
        screen.tracer(0)
        screen.onkey(snake.up, "w")
        screen.onkey(snake.down, "s")
        screen.onkey(snake.left, "a")
        screen.onkey(snake.right, "d")
        
        snake.follow()
        
        check_Food(food, snake, scorer)
     

def tap_to_change(x, y):
    global game_is_on, snake, food,scorer,life
    
    screen.clear() # removes initial image
    screen.bgcolor("#99C202")
    
    snake = Snake()
    food = Food()
    scorer = Scoreboard()
    life = Lives()
    
    game_is_on = True
    screen.update()
    run_game_loop()

def check_Food(food_obj, snake_obj,scorer_obj):
    if snake_obj.snake_head.distance(food_obj) < 15:
        print("Nom nom nom")
        food_obj.refresh()
        add_Score()
        scorer_obj.refresh()
        add_Snake()


def add_Score():
    scorer.score += 1
    print(scorer.score)
    
# def add_Lives():
#     life.live += 1
#     print(life.live)

def add_Snake():
    snake.addSnake()
    
screen.onscreenclick(tap_to_change)




screen.mainloop()
