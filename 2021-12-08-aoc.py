from aocd import get_data
import numpy as np
import re
import random


def challenge():
    data = get_data(day = 8)
    data = [d for d in data.split("\n")]
    c = 0
    print("Task 1: ")
    for line in data:
        _, l = line.split ("|")
        d =[ll for ll in l.split(" ")]
        for dd in d:
            if len(dd) in [2,4,3,7]:
                c += 1
    print(c)

    print("Task 2:")
    digits = {
        0: [1,1,1,0,1,1,1],
        1: [0,0,1,0,0,1,0],
        2: [1,0,1,1,1,0,1],
        3: [1,0,1,1,0,1,1],
        4: [0,1,1,1,0,1,0],
        5: [1,1,0,1,0,1,1],
        6: [1,1,0,1,1,1,1],
        7: [1,0,1,0,0,1,0],
        8: [1,1,1,1,1,1,1],
        9: [1,1,1,1,0,1,1]
    }

    def reverse(v):
        for d in digits:
            if digits[d] == v:
                return d

    def string_to_list(string, encoding):
        # encoding z.b. abcdegf
        return [int(letter in string) for letter in encoding]
    
    def decode(line, encoding):
        numbers = [string_to_list(l, encoding) for l in line.split(" ") if l is not "|"]
        if all(n in digits.values() for n in numbers):
            return True
        else:
            return False

    # s: summe aller vierstelligen outputs
    s = 0
    for line in data:
        encoding = "abcdefg"
        while(not decode(line, encoding)):
            encoding = ''.join(random.sample(encoding,len(encoding)))
        # jetzt ist encoding gefunden!
        _, l = line.split ("|")
        output = [reverse(string_to_list(ll, encoding)) for ll in l.split(" ") if ll.isalpha()]
        #print(encoding, output, s)
        s += int("".join(str(o) for o in output))
    print(s)
    
if __name__ == "__main__":
    challenge()