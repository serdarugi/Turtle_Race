from turtle import Turtle, Screen
import random

turtle_race = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the Race ? Enter a color :")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

while turtle_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            turtle_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win !!! The winner color is : {winning_color}")
            else:
                print(f"You lose !!! The winner color is :{winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
