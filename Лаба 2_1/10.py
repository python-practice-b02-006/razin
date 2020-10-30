import turtle as t
from math import pi, sin, cos

t.speed(10)
def ok():
    for i in range(180):
        t.forward(2*100*sin(pi/180))
        t.left(2)
        
for i in range(3):
    ok()
    t.left(180)
    ok()
    t.left(180+120)
    
t.done()