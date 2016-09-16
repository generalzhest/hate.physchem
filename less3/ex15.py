import sys

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

print(sys.getrecursionlimit())
x = 1
while True:
    y = fac(x)
    x += 1
print(x - 1)