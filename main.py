import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 500)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Type a color: ')
rainbow_turtles = {'red':[], 'orange':[], 'yellow':[], 'green':[], 'blue':[], 'indigo':[], 'violet':[]}

finish = False
black_turtle = Turtle()
black_turtle.ht()
black_turtle.penup()
black_turtle.setposition(280, 240)
black_turtle.pendown()
black_turtle.setposition(280, -230)


def setup_turtles():
    x = -280
    y = -200
    distance = 0
    for key in rainbow_turtles:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(key)
        new_turtle.penup()
        new_turtle.setposition(x,y)
        rainbow_turtles[key] = [distance, new_turtle]
        y += 70

def turtle_step (list_turtles):
    speed = random.randint(0,10)
    list_turtles[1].speed(speed)
    step = random.randint(0, 10)
    list_turtles[0] += step
    list_turtles[1].forward(step)


setup_turtles()

while not finish:
    for key in rainbow_turtles:
        update_turtle = rainbow_turtles[key]
        turtle_step(update_turtle)
        if update_turtle[0] >= 550:
            finish = True
            print(f"The '{key}' turtle WIN!")
            if user_bet.lower() == key:
                print("Congratulate, you've won!")
            else: print("You've lost!")
            break


screen.exitonclick()
