from turtle import Turtle, Screen

# Creating necessary objects
tim = Turtle()
screen = Screen()
tim.speed("fastest")


# Functions for the movement
def move_fd():
    tim.forward(10)


def move_bk():
    tim.backward(10)


def move_cw():
    tim.right(10)


def move_ccw():
    tim.left(10)


def world_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Call the listen method for Screen
screen.listen()

# Call the onkey method for the movements of turtle
screen.onkeypress(key="w", fun=move_fd)
screen.onkeypress(key="s", fun=move_bk)
screen.onkeypress(key="a", fun=move_cw)
screen.onkeypress(key="d", fun=move_ccw)
screen.onkeypress(key="c", fun=world_clear)

# Screen exit method
screen.exitonclick()
