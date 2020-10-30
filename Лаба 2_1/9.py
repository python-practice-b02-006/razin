import turtle as t

def ny(n, d):
    for i in range(n):
        t.left(360/n)
        t.forward(d)
        
d = 40
t.speed(10)
for i in range(10):
    ny(i+3, d)
    t.penup()
    t.forward(d/2)
    d = d + 10
    t.right(90)
    t.forward(d/4)
    t.right(90)
    t.forward(d/3)
    t.right(180)
    t.pendown()
    
t.done()