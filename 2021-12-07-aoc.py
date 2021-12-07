from aocd import get_data
import numpy as np
import re

# Task 1
def move_crabs_1(ll, i):
    s = 0
    for l in ll:
        s+=  abs(i - l)
    return(s)

# Task 2
def move_crabs_2(ll, i):
    s = 0
    for l in ll:
        j =  abs(i - l)
        s += j * (j+1) / 2
    return(s)

def challenge():
    data = get_data(day = 7)
    data = [int(d) for d in data.split(",")]
    #data = [16,1,2,0,4,2,7,1,2,14]
    mm = max(data)
    n = 10 ** 9
    m = 10 ** 9
    for i in range(mm):
        n = min(n, move_crabs_1(data, i))
        m = min(m, move_crabs_2(data, i))
    print(f"Task 1: {n} \nTask 2: {round(m)}")

if __name__ == "__main__":
    challenge()