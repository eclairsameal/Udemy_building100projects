import turtle
from check_states import CheckStates

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

check_states = CheckStates()


while check_states.correct < 50:
    title_correct = f"{check_states.correct}/50 States Correct"
    answer_state = screen.textinput(title=title_correct, prompt="What's another state's name?").title()
    #print(answer_state)
    if answer_state == "Exit":
        check_states.output_missing_states()
        break
    check_states.check_answer(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# # Get the coordinates of the mouse click (得到滑鼠按下的座標)

# turtle.mainloop()
# screen.exitonclick()
# The program will exit after clicking the mouse(按下滑鼠後會結束程式)
