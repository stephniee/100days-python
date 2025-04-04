from turtle import Turtle, Screen
import random

COLOR = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
game = True
# screen
while game:
    user_bet = screen.textinput(
        title="Make a bet!",
        prompt="Which turtle do you think will win the bet? Enter a color",
    )

    if user_bet is None or not user_bet.isalpha():
        raise TypeError("Only colors please!")
    # Generate turtles
    all_turtles = []

    vertical_y = -80
    for _ in range(0, len(COLOR)):
        tim = Turtle(shape="turtle")
        tim.color(COLOR[_])
        tim.penup()
        tim.goto(x=-240, y=vertical_y + _ * 40)
        all_turtles.append(tim)

    if user_bet:
        race_on = True

    while race_on:
        for turtle in all_turtles:
            turtle.pendown()
            if turtle.xcor() > 230:
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    play_again = screen.textinput(
                        title="Victory",
                        prompt=f"You've won the race! The winning color was {winning_turtle} Wanna play again? Y/N",
                    )
                    race_on = False

                else:
                     play_again =screen.textinput(title="Defeat",prompt=f"You've lost the race! The winning was color {winning_turtle} Wanna play again? Y/N",)
                     race_on = False
            movement = random.randint(1, 10)
            turtle.fd(movement)
    
    if play_again == 'N':
        game = False
    elif play_again == 'Y':
        screen.clear()
        game = True
        

screen.exitonclick()
