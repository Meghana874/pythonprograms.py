def fun(x,y):
    print(x,y)
    return x+y
print(fun(10,20))

def fun(x,y):
    return x+y
print(fun(10,20))

def fun(x,y):
    print(x+y)
fun(10,20)

def great(a,b):
    if a>b:
        return a
    else:
        return b
print(great(75,77))


def fun(*a):
    return  sum(a)
x=fun(1,7,8,6,5,3,2,8)
if x%2==0:
    print(f"even:{x}")
else:
    print(f"odd:{x}")

def fun4():
    print("hello")
y=fun4
fun4()
y()

def fun5(x,y):
    print(x+y)
c=fun5
print(c(10,45))
k=c(77,80)
print(k)
name=input("enter your name:")
s=f" name:{name}"
print(s)
