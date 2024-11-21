from math import sin, cos

def f1(x, y):
    return x+y


def f2(x,y):
    return (x**2)*y-0.5*(y**2)

def f3(x, y):
    return cos(x+y)


def findyn(x0, y0, h, slopefunc, n):
    i=0
    x_sub_n=x0
    y_sub_n=y0
    while i<n: 
        y_sub_n+=h*slopefunc(x_sub_n, y_sub_n)
        x_sub_n+=h
        i+=1
    return y_sub_n

