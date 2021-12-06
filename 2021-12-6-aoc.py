from aocd import get_data

def get_new_list(old_list):
    new_list = []
    for e in old_list:
        if e == 0:
            new_list.append(6)
            new_list.append(8)
        else:
            new_list.append(e-1)
    return new_list

def get_new_dict(old_dict):
    new_dict = {i:0 for i in range(9)}
    for i in range(9):
        if i == 0:
            new_dict[8] += old_dict[0]
            new_dict[6] += old_dict[0]
        else:
            new_dict[i-1] += old_dict[i]
    return new_dict

def challenge():
    data = get_data(day=6)
    data = [int(dd) for dd in data.split(",")]
    data_ = {d: data.count(d) for d in range(9)}
    print(data_)
    for i in range(256):
        data_ = get_new_dict(data_)
    print(sum(data_.values()))

challenge()