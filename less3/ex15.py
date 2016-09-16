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
    print (x)
    x += 1