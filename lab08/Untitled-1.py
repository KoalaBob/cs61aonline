def mutate_list(l):
    for item in l:
        if type(item)==list:
            item+=['koala']

L=[[1,2,3],2,[3,4,5]]
mutate_list(L)
print(L)
