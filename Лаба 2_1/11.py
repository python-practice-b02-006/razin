import turtle as t

t.left(90)
n = 50

def but(n):
    t.circle(n)
    t.left(180)
    t.circle(n)
    t.right(180)

for i in range(10):
    but(n)
    n += 5
    
t.done()