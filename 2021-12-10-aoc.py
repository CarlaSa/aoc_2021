from aocd import get_data
import numpy as np
from scipy.ndimage.measurements import label
import re
import random


def reduce_line(old_string):
    new_string =  re.sub("\(\)|\[\]|\<\>|\{\}", "", old_string)
    if len(new_string) < len(old_string):
        return True, new_string
    else:
        return False, new_string

def contains_corrupted(string):
    aa = [r"\(", r"\[", r"\<", r"\{"]
    bb = [r"\)", r"\]", r"\>", r"}"]
    regex = "|".join(aa[i] + bb[j] for i in range(4) for j in range(4) if i != j)
    found = re.findall(regex, string)
    if len(found) > 0:
        return True, found[0][1]
    else:
        return False, None
    
def get_score_2(s):
    s2 ={"(": 1, "[": 2, "{" :3, "<": 4}
    score = 0
    while s != "":
        s, c = s[:-1], s[-1]
        score = score * 5 + s2[c]
    return score

def challenge():
    data = get_data(day = 10)
    data = [d for d in data.split("\n")]
    score_dict_1 = {
        ")": 3, "]" : 57, "}": 1197, ">": 25137
    }
    score_1 = 0
    score_2 = []
    for d in data:
        m = True
        while(m):
            m, d = reduce_line(d)
        t, s = contains_corrupted(d)
        if t:
            # corrupted, find first
            score_1 += score_dict_1[s]
        else:
            # incomplete, complete
            if d == "":
                continue
            score_2.append(get_score_2(d))
    print(f"Task 1: {score_1}")
    print(f"Task 2: {sorted(score_2)[len(score_2) // 2]}")



if __name__ == "__main__":
    # s = "[({(<(())[]>[[{[]{<()<>>"
    # m = True
    # while(m):
    #     m, s = reduce_line(s)
    # print(s)
    # print(get_score_2(s))
    challenge()
    