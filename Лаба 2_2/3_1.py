from random import randint
import turtle as t


num = 20
step = 10000
a = 150
b = 0
t.tracer(0, 0)
t.hideturtle()
t.penup()
t.goto(a,a)
t.pendown()
t.goto(a,-a)
t.goto(-a,-a)
t.goto(-a,a)
t.goto(a,a)
t.update()
t.tracer(0, 0)
pool = [t.Turtle(shape='circle') for i in range(num)]
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(0,0), randint(0,0)
    b += 360/num
    unit.right(b)
t.update()


for i in range(step):
    for unit in pool:
        t.tracer(0, 0)
        unit.forward(5)
        if (unit.distance(a, unit.ycor()) <= 13) :
            unit.left(180-2*unit.heading())
        if (unit.distance(unit.xcor(), a) <= 13) :
            unit.left(360-2*unit.heading())
        if (unit.distance(-a, unit.ycor()) <= 13) :
            unit.right(180-2*(360-unit.heading()))
        if (unit.distance(unit.xcor(), -a) <= 13) :
            unit.right(180-2*(90-unit.heading()))
        t.update()
        
t.done()