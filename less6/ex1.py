import math
import random
import matplotlib.pyplot as plt

#subplot 1
plt.subplot(221)
random.seed(0)
n = 100
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

#subplot 2
plt.subplot(222)
random.seed(0)
n = 1000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

#subplot 3
plt.subplot(223)
random.seed(0)
n = 10000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

#subplot 4
plt.subplot(224)
random.seed(0)
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)

plt.show()