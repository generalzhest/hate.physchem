import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0, 230, 480, 690, 930, 1160, 1400, 1660]

v, p = np.polyfit(x, y, deg=1)
a, b, c = np.polyfit(x, y, deg=2)
print(v)
print(p)
print(a)
print(b)
print(c)

plt.errorbar(x, y, xerr=0.25, yerr=125)
plt.grid()
plt.show()