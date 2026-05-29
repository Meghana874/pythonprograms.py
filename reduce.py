from functools import reduce
st=['.','j','o','i','n','(',')']
k= reduce(lambda x,y:x+y,st)


from functools import reduce
l=[1,7,6,3,8,9,11,10]
k=reduce(lambda x,y:x if x>y else y,l)

c=[0,22,31,35,23]
k=list(map(lambda x:x%3,l))
f=list(filter(lambda x:x%3,l))
print(f)
print(k)
