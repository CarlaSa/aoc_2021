from aocd import get_data
import string
from collections import defaultdict

def grow(input, instructions):
    output = ""
    for i in range(len(input) - 1):
        two = input[i:i+2]
        output += input[i] + instructions[two]
    output += input[-1]
    return output

def grow_not_exp(input, instructions):
    output = defaultdict(int)
    for two, val in input.items():
        if val == 0:
            continue
        j = instructions[two]
        output[two[0] + j] += val
        output[j + two[1]] += val
    return output

def challenge():
    data = get_data(day = 14)
    inp, instructions = data.split("\n\n")
    instructions = {(a := d.split(" -> "))[0]: a[1]  for d in instructions.split("\n")}

    input = inp
    for i in range(5):
        input = grow(input, instructions)
        counts = {i: input.count(i) for i in set(list(input))}
        print(counts)
    print("Task 1")
    print(max(counts.values()) - min(counts.values()))

    input = {a+b: inp.count(a+b) for a in string.ascii_uppercase for b in string.ascii_uppercase}
    for i in range(5):
        input = grow_not_exp(input, instructions)
        counts = defaultdict(int)
        for i,v in input.items():
            counts[i[0]] += v
            counts[i[1]] += v
        counts[inp[0]] += 1
        counts[inp[-1]] += 1
        print(counts.items())
    print("Task 2")
    print(max(counts.values())/2 - min(counts.values())/2)
    
if __name__ == "__main__":
    challenge()
    