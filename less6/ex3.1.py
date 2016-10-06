import numpy as np

def get_percentile(values, bucket_number):
    A = [0.0]
    a = 100 / bucket_number
    for i in range(1,bucket_number):
        p = np.percentile(values, a)
        A.append(p)
        a += 100 / bucket_number
    return A

x = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
y = 5
print(get_percentile(x, y))