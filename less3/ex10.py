import turtle as t
t.shape('turtle')
for i in range(6):
    for j in range(360):
        t.forward(1)
        t.left(1)
    t.right(180 - ((6 - 2) * 180) / 6)