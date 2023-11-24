
import turtle
import pandas


screen = turtle.Screen()
screen.title("India state Game")
# giving image a path to main file
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# get x and y value if you dont have

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("all_states_india.csv")
all_state = data.state.to_list()

guessed_state = []

while len(guessed_state) < 29:

    answer_state = screen.textinput(title= f"{len(guessed_state)}/29 correct state",
                                    prompt="Whats the name of another sate").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_state:
                missing_states.append(state)
        # print(missing_states)

        missing_state_data = pandas.DataFrame(missing_states)
        missing_state_data.to_csv("states_to_learn.csv")

        break


    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# turtle.mainloop()
# turtle.exitonclick()