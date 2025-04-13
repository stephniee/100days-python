from turtle import Turtle, Screen
ALIGNMENT = "left"
FONT = ["Nokia Cellphone FC",30,"normal"]

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()  # Call the parent class's __init__ method
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("#000300")
        self.goto(-280, 230)
        self.write("SCORE:" + str(self.score), align=ALIGNMENT, font=FONT)
    def refresh(self):
        self.clear()  # Clear the previous score
         
        self.write("SCORE:" + str(self.score), align=ALIGNMENT, font=FONT)

class Lives(Turtle):
    
    def __init__(self):
        super().__init__()  # Call the parent class's __init__ method
        self.live = 3
        self.hideturtle()
        self.penup()
        self.color("#000300")
        self.goto(-280, 190)
        self.write("LIVES:" + str(self.live), align=ALIGNMENT, font=FONT)
    
    def refresh(self):
        self.clear()  # Clear the previous live
         
        self.write("LIVES:" + str(self.live), align=ALIGNMENT, font=FONT)