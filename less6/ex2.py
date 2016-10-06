import random

def f(x):
    if x >= -2 and x <= 2:
        return -x**2 + 4
    else:
        return 0

random.seed(0)
N = 100000
int = 0
a = 6 / N
for i in range(N):
    x = random.uniform(-3, 3)
    int += f(x)
print(a*int)