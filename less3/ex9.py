import turtle as t
import numpy as np
n = 3
for i in range(1, 11):
    a = 2 * i * 10 * np.sin(360 / (2 * n))
    for i in range (n):
        t.forward(a)
        t.left(180 - (n - 2) * (180 / n))
    t.right((180 - (n - 2) * (180 / n)) / 2)
    t.penup()
    t.forward(10)
    t.pendown()
    n += 1