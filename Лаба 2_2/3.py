from random import randint
import turtle as t


num = 2
step = 10
a = 300
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
    unit.speed(50)
    unit.goto(randint(-a, a), randint(-a, a))
    unit.right(randint(0, 360))
t.update()

for i in range(step):
    for unit in pool:
        t.tracer(0, 0)
        unit.forward(5)
        if (t.distance(a, t.ycor()) <= 30) :
            t.left(180-2*t.heading())
        print(t.ycor())
        t.update()
        
t.done()