import turtle

t = turtle.Turtle()

def move_up():
    t.goto(t.xcor(), t.ycor() + 30)


def move_down():
    t.goto(t.xcor(), t.ycor() - 30)
    
screen = turtle.Screen()

screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")



segments = []

direction = "up"
for i in range(5):
    t = turtle.Turtle()
    t.shape("square")
    t.penup()
    t.goto(-20*i, 0)
    segments.append(t)
