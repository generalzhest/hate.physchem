import turtle as t
import time
t.shape('turtle')
t.begin_fill()
for i in range(72):
    t.color("black", "yellow")
    t.forward(10)
    t.left(5)
t.end_fill()
t.left(90)
t.penup()
t.forward(175)
t.left(90)
t.forward(50)
t.pendown()
t.begin_fill()
t.color("black", "blue")
for i in range(72):
    t.forward(1)
    t.left(5)
t.end_fill()
t.left(180)
t.penup()
t.forward(100)
t.begin_fill()
for i in range(72):
    t.forward(1)
    t.right(5)
t.end_fill()
t.left(180)
t.penup()
t.forward(45)
t.left(90)
t.forward(30)
t.pendown()
t.width(5)
t.color("black")
t.forward(50)
t.left(90)
t.penup()
t.forward(70)
t.right(90)
t.pendown()
t.color("red")
t.width(5)
for i in range(23):
    t.forward(10)
    t.right(8)
t.color("black")
t.penup()
t.left(90)
t.forward(100)
t.right(135)
t.pendown()
t.stamp()
t.penup()
t.forward(500)
time.sleep(10)