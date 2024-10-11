def a_then_b(a,b):
    yield from a 
    yield from b 

print(next(a_then_b([3,4],[5,6])))