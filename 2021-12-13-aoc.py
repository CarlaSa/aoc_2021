from aocd import get_data
import re

def fold(dots, axis, num):
    num = int(num)
    new_dots = []
    for d in dots:
        x, y = d
        if axis == "x":
            if x < num:
                x = x
            else:
                x = num - (x - num)
        elif axis == "y":
            if y  < num:
                y = y
            else:
                y = num - (y - num)
        if [x,y] not in new_dots:
            new_dots.append([x,y])
    return new_dots

def image(dots):
    xx  = max(d[0] for d in dots)
    yy = max(d[1] for d in dots)
    string = [["#" if [x,y] in dots else " " for x in range(xx+1)] for y in range(yy+1)]
    string = ["".join(dd) for dd in string]
    string = "\n".join(string)
    print(string)

def challenge():
    data = get_data(day = 13)
    #data = "6,10\n0,14\n9,10\n0,3\n10,4\n4,11\n6,0\n6,12\n4,1\n0,13\n10,12\n3,4\n3,0\n8,4\n1,10\n2,14\n8,10\n9,0\n\nfold along y=7\nfold along x=5"
    dots, instructions = data.split("\n\n")
    dots = [[int(d) for d in dd.split(",")] for dd in dots.split("\n")]
    instructions = re.findall(r"(x|y)=(\d+)", instructions)

    i = instructions[0]
    dots_ =fold(dots, i[0], i[1])
    print(f"Task 1: {len(dots_)}")
    for i in instructions:
        dots = fold(dots, i[0], i[1])
    print("Task 2:")
    image(dots)

if __name__ == "__main__":
    challenge()