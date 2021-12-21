from itertools import permutations
from aocd import get_data
import re
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def to_number(window):
    s = 0
    for i,x in enumerate(window.flatten()[::-1]):
        s += x * 2**i
    return(s)

def enhance(image, enh):
    def lookup(x):
        x = enh[x]
        return 1 if x == "#" else 0
    padded_image = np.pad(image, (2,2), "edge",)
    windows = sliding_window_view(padded_image, (3,3))
    new = np.array([
        [lookup(to_number(window)) for window in line]
        for line in windows
    ])
    return new


def challenge():
    data = get_data(day = 20)    
    
    #data = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#\n\n#..#.\n#....\n##..#\n..#..\n..###"
    enh, image = data.split("\n\n")
    image = image.split("\n")
    image = np.array([[1 if x == "#" else 0 for x in line] for line in image])
    image =  np.pad(image, (10,10), "constant", constant_values = (0,0))
    for _ in range(50):
        image = enhance(image, enh)
    image = image[8:-8, 8:-8]
    print(image)
    print(np.sum(image))



if __name__ == "__main__":
    challenge()
