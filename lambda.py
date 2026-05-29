l=[1,7,8,9,12,14,21,22,63,66]
k=list(map(lambda x:x**3,l))
print(k)

l=[1,7,8,9,12,14,21,22,63,66]
k=list(filter(lambda x:x%4,l))
print(k)

k=list(filter(lambda x:x%4,map(lambda x:x**3,l)))
print(k)


nums=[1,2,3,4]
k=list(map(lambda x:x+2,nums))
print(k)
nums=[1,2,3,4,5,6]
k=list(filter(lambda x:x%2==0,nums))
print(k)

from functools import reduce
x=[1,2,3,4]
k=reduce(lambda x,y:x+y,nums)
print(k)

l=[21,3,2,5,22,6,32]
k=sorted(l,key=lambda x:x%3)
print(k)


l=[23,21,27,28,44,46]
k=sorted(l,key=lambda x:x%7,reverse=True)
print(k)



l=[23,21,27,28,44,46]
k=sorted(l,key=lambda x:x%7,reverse=False)
print(k)
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


