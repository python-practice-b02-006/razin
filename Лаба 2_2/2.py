import turtle as t


t.speed(10)
a = 50


def _0(x, y):
    global a
    x[0] += a
    t.goto(x[0], y[0])
    y[0] -= 2*a
    t.goto(x[0], y[0])
    x[0] -= a
    t.goto(x[0], y[0])
    y[0] += 2*a
    t.goto(x[0], y[0])
    t.penup()
    x[0] += 2*a
    t.goto(x[0], y[0])
    t.pendown()


def _1(x, y):
    global a
    t.penup()
    y[0] -= a
    t.goto(x[0], y[0])
    t.pendown()
    x[0] += a
    y[0] += a
    t.goto(x[0], y[0])
    y[0] -= 2*a
    t.goto(x[0], y[0])
    t.penup()
    x[0] += a
    y[0] += 2*a
    t.goto(x[0], y[0])
    t.pendown()
    
    
def _4(x, y):
    global a
    y[0] -= a
    t.goto(x[0], y[0])
    x[0] += a
    t.goto(x[0], y[0])
    y[0] += a
    t.goto(x[0], y[0])
    y[0] -= 2*a
    t.goto(x[0], y[0])
    t.penup()
    x[0] += a
    y[0] += 2*a
    t.goto(x[0], y[0])
    t.pendown()
    
    
def _7(x, y):
    global a
    x[0] += a
    t.goto(x[0], y[0])
    x[0] -= a
    y[0] -= a
    t.goto(x[0], y[0])
    y[0] -= a
    t.goto(x[0], y[0])
    t.penup()
    x[0] += 2*a
    y[0] += 2*a
    t.goto(x[0], y[0])
    t.pendown()
    
    

x = [-275]
y = [50]
l = (_1(x, y), _4(x, y), _1(x, y), _7(x, y), _0(x, y), _0(x, y))

t.done()