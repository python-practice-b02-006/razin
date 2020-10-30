import turtle as t

t.speed(10)
f = 14.14213562
x = f
for i in range(10):
    for j in range(4):
        t.forward(x)
        t.left(90)
    t.up()
    t.right(90)
    t.forward(7.071067812)
    t.right(90)
    t.forward(7.071067812)
    t.left(180)
    t.down()
    x = f*(i+2)
    
t.done()