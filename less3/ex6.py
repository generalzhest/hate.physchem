import turtle as t
n = int(input())
t.shape('turtle')
for i in range(n):
    t.forward(50)
    t.stamp()
    t.left(180)
    t.forward(50)
    t.left(360/n)