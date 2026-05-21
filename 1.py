def fun4(x=10,y=70,z=50):
    print(x,y,z)
    print(x+y+z)
fun4(70,70,70)
fun4()

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))



a=20
b=30
c=40
print(a,b,c ,sep='@' ,end='@')
def fun3(a,b,c,d):
    print(a,b,c,d)
def fun2(**b):
    print(b)
    fun3(**b)
fun2(a=75,b=30,c=40,d=70)

colors = ("red", "blue", "green")
print(colors)
print(type(colors))


items = {1, 2, 3, 3}
print(items)
print(type(items))

student = {
    "name": "Pinky",
    "age": 21
}

print(student)
print(type(student))

def greet():
    print("Welcome")

greet()


def add(a, b):
    print(a + b)

add(10, 20)


price = 99.5
print(price)
print(type(price))

a = 10
print(a)
print(type(a))


l=[1,2,3]
k=l
l.append(10)
k.append(50)
print(l,k)
