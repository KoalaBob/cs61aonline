def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

a=filter(lambda n: n > 4, gen_fib())



def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    iterlist=list(t)
    L=[]
    for i in range(len(iterlist)):
        if i+1 != len(iterlist):
            L.append(iterlist[i+1]-iterlist[i])
    return iter(L)

print(list(differences(iter([5, 2, -100, 103]))))
print(next(differences(iter([39,100]))))