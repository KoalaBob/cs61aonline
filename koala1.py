from math import exp, cos, sin, pi

def trapezoid(a,b,n,function):
    total=0
    interval=(a-b)/n
    count=b
    for i in range(n):
        count+=interval
        count=round(count,6)
        total+=2*function(count)
    return round((interval/2)*(total+function(b)-function(a)),6)

def midpoint(a,b,n,function):
    total=0
    interval=(a-b)/n
    count=b+interval/2
    for i in range(n-1):
        count+=interval
        count=round(count,6)
        total+=function(count)
    return round(interval*(total+function(b+interval/2)),6)

def simpson(a,b,n,function):
    total=0
    interval=(a-b)/n
    count=b
    for i in range(1,n):
        count+=interval
        count=round(count,6)
        if i%2!=0:
            total+=4*function(count)
        else:
            total+=2*function(count)
    return round((interval/3)*(total+function(b)+function(a)),6)
        

def approximate_integration(*arg):
    return f"The trapzoid sum is {trapezoid(*arg)}, the midpoint sum is {midpoint(*arg)}, the simpson sum is {simpson(*arg)}" 



def q9(x):
    return exp(x)/(1+x**2)

def q10(x):
    return (1+cos(x))**(1/3)

def q16(t):
    return sin(t)/t

# print(approximate_integration(pi/2, 0, 4, q10))
# print(approximate_integration(3,1,4,q16))




pairs=[[1,2],[2,2],[3,2],[4,4]]
def samecount(L):
    count=0
    for x, y in L:
        print('this is x, y', x, y)
        if x==y:
            
            count+=1
    return count

print(samecount(pairs))