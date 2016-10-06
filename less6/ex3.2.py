import numpy as np

def get_percentile(values, bucket_number):
    percentiles = [0.0]
    a = 100 / bucket_number
    for i in range(1,bucket_number):
        p = np.percentile(values, a)
        percentiles.append(p)
        a += 100 / bucket_number
    return percentiles

def get_percentile_number(value, percentiles):
    for i in percentiles:
        if value > i:
            continue
        else:
            break
    x = percentiles.index(i) - 1
    return x

values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
bucket_number = 4
percentiles = get_percentile(values, bucket_number)
print(percentiles)
print(get_percentile_number(2.5, percentiles))
print(get_percentile_number(5.5, percentiles))
print(get_percentile_number(100, percentiles))