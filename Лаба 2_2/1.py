import turtle as t
import random


t.speed(10)
for i in range(200):
    t.forward(random.random()*50)
    t.left(random.random()*360)
    

t.done()