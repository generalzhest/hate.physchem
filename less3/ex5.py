import  turtle as t
t.shape('turtle')
for i in range(10):
    for j in range(4):
        t.forward((i * 2 + 1) * 10)
        t.left(90)
    for k in range(2):
        t.right(90)
        t.penup()
        t.forward(10)
        t.pendown()
    t.left(180)