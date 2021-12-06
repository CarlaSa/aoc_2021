from aocd import get_data
import re

def day_1_1(data):
    data = get_data(day = 1)
    data_list = data.split()
    old = None
    n = 0
    for d in data_list:
        if old == None:
            old = int(d)
            continue
        if int(d) > old:
            n += 1
        old = int(d)
    return(n)

def day_1_2(data):
    data_list = [int(d) for d in data.split()]
    old = []
    n = 0
    for d in data_list:
        if len(old) < 3:
            old.append(d)
            continue
        new = [old[1], old[2], d]
        if sum(new) > sum(old):
            n += 1
        old = new
    return n

def day_2_1(data):
    f,u,d= [a + r'\w*\ (\d)' for a in 'fun']
    v = lambda p: sum([int(n) for n in re.findall(p, data)])
    return v(f) * (v(d) - v(u))

def day_2_2(data):
    v = lambda p: tuple( int(x) if a in p else 0 for a in "fun" for x in re.findall(r"\d", p))
    a, h, d = 0,0,0
    for dd in data.split("\n"):
        r = v(dd)
        a,h,d = a - r[1] + r[2], h + r[0], d + a * r[0]
    return h * d

if __name__ == "__main__":
    d = 2
    f = day_2_2
    data = get_data(day = d)
   #data = "forward 5 \n down 5 \n forward 8 \n up 3 \n down 8 \n forward 2"
    print(f(data))
    