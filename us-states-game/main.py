import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# get coordinates of map location


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed", prompt="What's another state's name").title()
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        # x_cor = data[data.state == answer_state].x
        # y_cor = data[data.state == answer_state].y
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    if answer_state == "Exit":
        # missing_state = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        missing_state = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break


