from aocd import get_data
import numpy as np
import re
import random

def step(oct_old):
    flash_coords = []
    oct_new = oct_old + 1
    while np.any(oct_new > 9):
        for (i,j) in np.argwhere(oct_new > 9):
            if (i,j) in flash_coords:
                oct_new[i,j] = 0
                continue
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if ii < 0 or jj < 0 or ii > 9 or jj > 9:
                        continue
                    else:
                        oct_new[ii,jj] += 1
            flash_coords.append((i,j))
            oct_new[i,j] = 0
    for (i,j) in flash_coords:
        oct_new[i,j] = 0
    return oct_new, len(flash_coords)

def challenge():
    data = get_data(day = 11)
    data = np.array([[int(d) for d in dd]  for dd in data.split("\n")])
    #data = ["11111", "19991","19191", "19991","11111"]
    #data = ["5483143223", "2745854711","5264556173","6141336146","6357385478","4167524645","2176841721","6882881134","4846848554","5283751526"]
    #data = np.array([[int(d) for d in dd] for dd in data])
    flashes = 0
    for i in range(300):
        data, f = step(data)
        flashes += f
        if i == 99:
            print(f"Task 1: {flashes}")
        if f == 100:
            print(f"Task 2: {i + 1}")
            break


if __name__ == "__main__":
    challenge()