import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="What's your bet?", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turts = []
pos_y = -100

for turt_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.goto(x=-230, y=pos_y)
    turt.color(colors[turt_index])
    pos_y += 30
    all_turts.append(turt)

if user_bet:
    race_on = True

while race_on:
    for turt in all_turts:
        if turt.xcor() > 235:
            race_on = False
            winner = turt.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The {winner} turtle is the winner!")
        distance = random.randint(0, 10)
        turt.forward(distance)

screen.exitonclick()
