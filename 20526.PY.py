

def fun(*a):
    print(sum(a[::2]))
    a[1::2]
fun(2,3,45,667,77)
def fun(*a):
    print(a)

fun(10,20,30)

def fun(*a):
    print(sum(a))

fun(1,2,3,4)

def fun(*a):
    for i in a:
        if i % 2 == 0:
            print(i)

fun(1,2,3,4,5,6)

def fun(*a):
    print(a[::3])

fun(1,2,3,4,5,6)


def fun(*a):
    print(a[1::2])

fun(1,2,3,4,5,6)

def fun(*a):
    print(sum(a[::2]))

fun(2,3,45,667,77)

def fun(*a):
    print(a)
    print(*a)
fun(10,20,30,40,60)

def fun2(**b):
    print(b)
fun2(a=75,b=30,c=40,d=70)

def fun3(a,b,c,d):
    print(a,b,c,d)
def fun2(**b):
    print(b)
    fun3(**b)
fun2(a=75,b=30,c=40,d=70)

def fun5(*a,**b):
    print(a,b,sep="\n")
fun5(1,7,3,4,6,8,a=75,b=30)

def fun6(*a):

    print(sum(a))

fun6(1,7,8,25,30,60,70)

def fun7(*a):
    i=0;s=0;
    while i<len(a):
        if a[i]%2==0:
            s+=a[i]
        i+=1
    print(s)
fun7(1,7,8,25,30,60,70)



