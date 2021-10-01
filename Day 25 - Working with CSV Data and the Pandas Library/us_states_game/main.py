import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
# Get the coordinates of the mouse click (得到滑鼠按下的座標)

turtle.mainloop()
# screen.exitonclick()
# The program will exit after clicking the mouse(按下滑鼠後會結束程式)
