import turtle

t = turtle.Turtle()
t.speed('fastest')

def half_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

t.color('red', 'pink')
t.begin_fill()
half_heart()
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
half_heart()
t.end_fill()

turtle.done()
