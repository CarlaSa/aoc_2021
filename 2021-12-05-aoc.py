from aocd import get_data
import numpy as np
import re

def get_points(x1,y1,x2,y2):
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        return [(x1,y) for y in range(y1, y2+1)]
    if y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        return [(x, y1) for x in range(x1, x2+1)]
    else:
        a = x1 < x2
        b = y1 < y2
        xx2 = x2+1 if a else x2 -1
        yy2 = y2+1 if b else y2-1
        r1 = 1 if a else -1
        r2 =  1 if b else -1
        return [(x,y) for (x,y) in zip(range(x1, xx2, r1), range(y1, yy2, r2))]
        

def challenge():
    data = get_data(day = 5)
    n = 0
    pipe_points = {}
    for d in data.split("\n"):
        x1, y1, x2, y2 = re.split(r"\,| -> ", d)
        p = get_points(int(x1), int(y1), int(x2), int(y2))
        for pp in p:
            if pp in pipe_points:
                pipe_points[pp] += 1
                if pipe_points[pp] == 2:
                    n += 1
            else:
                pipe_points[pp] = 1
    print(n)

challenge()
