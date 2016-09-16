import turtle as t
import numpy as np

n = 3
for i in range(1, 11):
    a = 2 * i * 20 * np.sin((2 * np.pi) / (2 * n))
    for i in range(n):
        t.forward(a)
        t.left(180 - (n - 2) * (180 / n))
    t.right((180 - (n - 2) * (180 / n)) + ((n - 2) * 180) / (2 * n))
    t.penup()
    t.forward(20)
    t.left(180 - ((n - 1) * 180) / (2 * (n + 1)))
    t.pendown()
    n += 1