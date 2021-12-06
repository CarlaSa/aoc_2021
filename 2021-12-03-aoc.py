import numpy as np
from aocd import get_data

def challenge1():
    count_ = {i: [0,0] for i in range(12)}
    data = get_data(day = 3)

    for d in data.split("\n"):
        for i, dd in enumerate(d):
            count_[11 - i][int(dd)] += 1

    gamma = 0
    epsilon = 0
    for i in range(12):
        maxx = np.argmax(count_[i])
        minn = np.argmin(count_[i])
        gamma += maxx * (2 **i)
        epsilon += minn * (2 **i)

    power = gamma * epsilon
    print(power)

    data_o2 = [d  for d in data.split("\n")]
    data_co2 = [d  for d in data.split("\n")]
    
    def modify_data(data_, f , c):
        for i in range(12):
            if len(data_) == 1:
                break
            ar = [x[i] for x in data_]
            unique, counts = np.unique(ar, return_counts=True)
            if len(counts) == 1:
                continue
            if counts[0] == counts[1]:
                m = c
            else:
                m = f(counts)
            data_ = [d for d in data_ if int(d[i]) == m]
        return data_
    
    data_o2 = modify_data(data_o2, f = np.argmax, c = 1)
    data_co2 = modify_data(data_co2, f = np.argmin, c = 0)


    o2 = 0
    co2 = 0

    for i in range(12):
        o2 += int(data_o2[0][11-i]) * (2 **i)
        co2 += int(data_co2[0][11-i]) * (2 **i)

    lsr = o2 * co2
    print(lsr)


challenge1()