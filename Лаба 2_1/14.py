import turtle as t

def stars(n):
    t.left(180 - (180 / n))
    t.forward(200)

for i in range(7):
    stars(7)
t.penup()
t.forward(300)
t.pendown()
for i in range(11):
    stars(11)
    
t.done()