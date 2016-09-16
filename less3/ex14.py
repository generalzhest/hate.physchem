import turtle as t
import time
n = int(input())
a = 100
b = (180 - ((180 * (n - 2)) / ((n - 2) * n)))
for i in range(n):
    t.forward(a)
    t.right(b)
time.sleep(10)