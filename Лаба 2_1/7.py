import turtle as t
from math import pi, sin, cos

for i in range(300):
    a = i/10
    x = 10 * a * cos(a)
    y = 10 * a * sin(a)
    t.goto(x, y)

t.done()