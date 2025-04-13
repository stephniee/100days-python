from turtle import Screen 
from Snake import Snake
from Food import Food
from Score import Scoreboard, Lives


import pygame 
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#99C202")
screen.bgpic("Day20/assets/snake.gif")
screen.title("My Snake Game")
screen.tracer(0)
pygame.mixer.init() 

game_is_on = False
snake = None
food = None
scorer = None
life = None
 
pygame.mixer.music.load("Day20/assets/russian-roulette.mp3")
sound = pygame.mixer.Sound("Day20/assets/get-point.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

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
        check_Tail()
        check_Collision()
        game_over()
     

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
        play_eat_sound()
        food_obj.refresh()
        add_Score()
        scorer_obj.refresh()
        add_Snake()

def add_Score():
    scorer.score += 1
    print(scorer.score)
    
def check_Collision():
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        print("You hit a wall")
        reduce_life()

def check_Tail():
    
    for i, segment in enumerate(snake.snake_body[1:], start=1):  # skip head at in x 0
        dist = snake.snake_head.distance(segment)
 
        if dist < 10:
            print("Hit ur tail")
            reduce_life()
            break

def reduce_life():
    life.live -= 1
    life.refresh()
    flash_snake(snake)
    flash_screen()

def game_over():
    global game_is_on
    if life.live == 0:
        game_is_on = life.game_over()
    
# def add_Lives():
#     life.live += 1
#     print(life.live)
def flash_screen(times=3, delay=0.1):
    original_color = screen.bgcolor()
    for _ in range(times):
        screen.bgcolor("white")  # flash color
        screen.update()
        time.sleep(delay)
        screen.bgcolor(original_color)  # restore original
        screen.update()
        time.sleep(delay)
        
def flash_snake(snake, times=3 ):
    for _ in range(times):
        for segment in snake.snake_body:
            segment.color("red")
    time.sleep(0.1)
    for _ in range(times):
        for segment in snake.snake_body:
            segment.color("#000300")
def add_Snake():
    snake.addSnake()

def play_eat_sound():
    sound.play()


screen.onscreenclick(tap_to_change)




screen.mainloop()
