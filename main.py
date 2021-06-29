import turtle
import pandas
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

score = turtle.Turtle()
score.hideturtle()
score.penup()

count = 0
guessed_states = []
end = False
file = open("states_to_learn.txt", "a")
file.truncate(0)
while not end:
    answer = screen.textinput(title=f"{count} / 50 Correct", prompt="What's the name of another state?").title()

    if answer == "Exit":
        end = True

    elif answer in str(data.state) and answer not in guessed_states:
        row = data[data.state == answer]
        x = int(row["x"])
        y = int(row["y"])
        score.goto(x, y)
        score.write(arg=answer, font=("ariel", 8, "normal"))
        count += 1
        guessed_states.append(answer)

    if count == 50:
        end = True

for state in data.state:
    if state not in guessed_states:
        file.write(state + "\n")
file.close()

