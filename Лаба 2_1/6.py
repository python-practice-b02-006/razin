import turtle as t

t.speed(10)
n = 12
for i in range(n):
    t.forward(100)
    t.dot(10, "red")
    t.left(180)
    t.forward(100)
    t.left(180-360/n)

t.done()