x=10+5
print(x)
my_list=[1,2,3]
my_list.append(4)
print(my_list)
name="python"
print(name[0])
print(name[1:4])
print(name.upper())




def say_hello():
    print("welcome to python!")
say_hello()


def add(a,b):
    return a+b
result = add(5,3)
print(result)

def area_of_rectangle(length, width):
    return length * width

area = area_of_rectangle(6, 4)
print(area)

def test():
    print("hello")
result=test()
print(result)


def mul(a,b,c):
    return a*b*c
print(mul(5,7,8))

def pet(animal,name):
    print(f'animal:{animal},name:{name}')
    print("dog","fox")