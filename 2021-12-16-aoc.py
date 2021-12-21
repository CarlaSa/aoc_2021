from aocd import get_data
import numpy as np


def unzip(data):
    d = {
        "0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", 
        "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", 
        "8" : "1000", "9" : "1001", "A" : "1010", "B" : "1011", 
        "C" : "1100", "D" : "1101", "E" : "1110", "F" : "1111"
    }
    new_data = ""
    for dd in data:
        new_data += d[dd]
    return new_data

def get_number(binary):
    return sum(int(v) * 2**i for i,v in enumerate(binary[::-1]))

def decode_structure(s):
    version = s[0:3]
    type_id = s[3:6]
    # literal string
    if type_id == "100":
        num = ""
        for i in range(len(s)): # range too long but break first
            group = s[6+i*5: 11+i*5]
            num += group[1:5]
            if group[0] == "0":
                break
        rest = s[11+i*5:]
        #print(num)
        #print(get_number(num))
        # print(rest)
        return [version],  rest, 11+i*5, get_number(num), str(get_number(num))
    # operator
    else:
        operation = {
            "000": np.sum, "001": np.prod, "010": min, "011": max, 
            "101": lambda x: 1 if x[0] > x[1] else 0,
            "110": lambda x: 1 if x[0] < x[1] else 0,
            "111": lambda x: 1 if x[0] == x[1] else 0,
        }[type_id]
        v_ids = []
        if s[6] == "0":
            lenght = s[7:7+15]
            lenght = get_number(lenght)
            rest = s[22: 22 + lenght]
            m = 0
            numbers = []
            o = []
            while m < lenght:
                v, rest, i, num, out = decode_structure(rest)
                v_ids += v
                numbers.append(num)
                m += i
                o.append(out)
            return [version, v_ids], s[22 +lenght:], 22+lenght, operation(numbers),f"{type_id}({','.join(oo for oo in o)})"
        else:
            num_packages = s[7:7+11]
            num_packages = get_number(num_packages)
            rest = s[18:]
            m = 18
            o = []
            numbers = []
            for _ in range(num_packages):
                v, rest, i, num, out  = decode_structure(rest)
                m += i
                v_ids += v
                numbers.append(num)
                o.append(out)
            return [version, v_ids], s[m:], m, operation(numbers),  f"{type_id}({','.join(oo for oo in o)})"


def challenge():
    data = get_data(day = 16)
    # with open('input (1).txt') as f:
    #     data = f.readlines()[0].split("\n")[0]
    #data = "9C0141080250320F1802104A08"
    #data = "04005AC33890"
    #data = "D2FE28"
    #data = "9C005AC2F8F0"
    data = unzip(data)
    #data = "000100110011010111011110001011010101101111010100000"
    #print(data)
    d = decode_structure(data)

    def recursive_sum(nested):
        if isinstance(nested, str):
            return get_number(nested)
        return sum(recursive_sum(s) for s in nested)

    print(recursive_sum(d[0]))
    print(d[3])
    #print(d[4])

if __name__ == "__main__":
    challenge()