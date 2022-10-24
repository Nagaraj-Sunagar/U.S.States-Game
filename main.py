from tokenize import blank_re
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State guess game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data["state"].tolist()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guess_states)}/50 States Correct", prompt="What's another states name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()
