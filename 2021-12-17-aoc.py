from itertools import product
from aocd import get_data
import re

def step(x,y, x_vel, y_vel):
    x+= x_vel
    y+= y_vel
    x_vel = x_vel + (x_vel <= 0) - (x_vel >= 0)
    y_vel += -1
    return x,y,x_vel, y_vel

def in_target(x,y, xx, yy):
    return (x[0] <= xx and xx <= x[1]) and (y[0] <= yy and yy <= y[1])

def fly(x_vel, y_vel, xx, yy):
    y_max = 0
    x, y = 0,0
    while (x < xx[1] and y >= yy[0]):
        x,y,x_vel, y_vel = step(x,y,x_vel, y_vel)
        print(x,y)
        y_max = max(y, y_max)
        if in_target(xx,yy,x,y):
            return y_max
    return -10000

def x_vel_range(xx):
    ran = []
    for x_vel in range(-10,100):
        x_vel_copy= x_vel
        x = 0
        while (x >= 0 and x < xx[1]):
            x+= x_vel
            x_vel = x_vel + (x_vel <= 0) - (x_vel >= 0)
            if xx[0] <= x and x <= xx[1]:
                ran.append(x_vel_copy)
            if x_vel == 0:
                break
    return (min(ran), max(ran))

def y_vel_range(yy):
    ran = []
    for y_vel in range(-500,300):
        y_vel_copy= y_vel
        y = 0
        while( yy[0] <= y):
            y+= y_vel
            y_vel += -1
            if yy[0] <= y and y <= yy[1]:
                ran.append(y_vel_copy)
    return (min(ran), max(ran))

def challenge():
    data = get_data(day = 17)
    #data = "target area: x=20..30, y=-10..-5"
    x, y = re.findall(r"\w=(-?\d+\.\.-?\d+)", data)
    xx, yy = [int(xx) for xx in x.split("..")], [int(yy) for yy in y.split("..")]
    
    x_range = x_vel_range(xx)
    y_range = y_vel_range(yy)
    print(x_range, y_range)
    y_max = 0
    m = 0
    for x_vel in range(x_range[0], x_range[1]+ 1):
        for y_vel in range(y_range[0], y_range[1]+ 1):
            temp =  fly(x_vel, y_vel, xx, yy)
            if temp > -10000:
                m+= 1
            if temp > y_max:
                y_max = temp
                #print(temp, x_vel, y_vel)
    print(y_max)
    print(m)



if __name__ == "__main__":
    challenge()