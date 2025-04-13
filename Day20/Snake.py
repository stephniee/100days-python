from turtle import Screen, Turtle
import time
HORIZONTAL_SPACE = -20
MOVE_DISTANCE = 20

# ANGLES
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    # health = represents how many lives the snake has 
    # snake_body = how long the snake is (list)
    def __init__(self):
        self.snake_body = []
        self.createSnake()
        self.snake_head = self.snake_body[0]
        self.snake_tail = self.snake_body[-1]
  
    def createSnake(self):
        for _ in range(0, 3):
            snake = Turtle(shape="square")
            snake.color("#000300")
            snake.penup()
            snake.goto(x=0 + (_ *HORIZONTAL_SPACE), y=0)
            self.snake_body.append(snake)
    
        # self.health = health
    def addSnake(self):
            snake = Turtle(shape="square")
            snake.color("#000300")
            snake.penup()
            tail_position = self.snake_body[-1].position()
            snake.goto(tail_position)
            self.snake_body.append(snake)
        
    def follow(self): 
        # makes snake move forwards following the body from end to head:
        # Basically last body -> middle pos
        # Middle body -> Center   
        for snake in range(len(self.snake_body)-1,0,-1):
            pos_x = self.snake_body[snake - 1].xcor()
            pos_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(pos_x,pos_y)
        self.snake_head.forward(MOVE_DISTANCE) 
    
    def get_head(self):
        return self.snake_head
    
 
 
  # or your normal color
 
  
        
    # Movement Methods
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
       
    def down(self):
         if self.snake_head.heading() != UP:
             self.snake_head.setheading(DOWN) 
 
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT) 
   
              

   