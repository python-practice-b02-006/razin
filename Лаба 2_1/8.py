import turtle as t

x=5
for i in range(100):
    t.forward(x)
    t.left(90)
    x = x + 5

t.done()