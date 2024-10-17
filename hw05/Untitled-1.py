def f(x):
    answer=next(x)
    while True:
        yield answer

a=iter([1,2,3,4,5,6,7,8])
I=f(a)
print([next(I) for _ in range(4)])
