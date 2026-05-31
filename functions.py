#functions
def say_hello():
    print("Welcome to Python!")

say_hello()
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

def test():
    print("Hello")

x = test()
print(x)
def test():
    print("Hello")
    return None

def area_of_rectangle(length, width):
    return length * width

area = area_of_rectangle(6, 4)
print(area)

def multiply(a, b, c):
    return a * b * c
#PARAMETERS
print(multiply(2, 3, 4))

def describe_pet(animal, name):
    print("My", animal, "is named", name)

describe_pet("dog", "Tommy")
def power(base, exponent):
    return base ** exponent

print(power(2, 3))

def pet(animal, name):
    print(f"animal:{animal}, named:{name}")

pet("dog", "Tommy")

def full_name(first, middle, last):
    return first + " " + middle + " " + last

name = full_name("Pinky", "Kumari", "Reddy")
print(name)

def full_name(first, middle, last):
    return f"{first} {middle} {last}"

print(full_name("Pinky", "Kumari", "Reddy"))

name = full_name("Pinky", "Kumari", "Reddy")
print(name.upper())
#POSITIONAL ARGUMENTS
def intro(name, city, hobby):
    print(f" name {name}. {city}. {hobby}.")

intro("Pinky", "Hyderabad", "Reading")
def subtract(a, b):
    return a - b

print(subtract(10, 3))
print(subtract(3, 10))

def add(a, b):
    print(a, b)

add(10, 20)

def bio(first_name, last_name, age):
    print(f"{first_name} {last_name} is {age} years old.")

bio("Pinky", "Reddy", 21)

def student(name, age):
    print(name, age)

student("Pinky", 21)

#KEYWORD ARGUMENTS
def send_email(to, subject, body):
    print("To:", to)
    print("Subject:", subject)
    print("Body:", body)

send_email(
        subject="Meeting",
        body="Please attend the meeting.",
        to="pinky@gmail.com"
    )

def create_profile(username, email, age):
    print(username)
    print(email)
    print(age)

create_profile(
    age=21,
    username="Pinky",
    email="pinky@gmail.com"
)
#default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))
def connect(host, port=3306, protocol='TCP'):
    print(host, port, protocol)

connect("localhost")
connect("localhost", 8080)
connect("localhost", 8080, "UDP")

def func(age, name='Guest'):
    print(name, age)
def greet(name):
    print("Hello", name)
def add_all(*args):
    print(args)

add_all(10, 20, 30)

def add_all(*args):
    total = 0

    for i in args:
        total += i

    return total

print(add_all(10, 20))
print(add_all(10, 20, 30))
print(add_all(10, 20, 30, 40))

def info(**kwargs):
    print(kwargs)

info(name="Pinky", age=21)
def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

info(name="Pinky", age=21, city="Hyderabad")

#arbitary parameters
def multiply_all(*args):
    product = 1

    for num in args:
        product *= num

    return product

print(multiply_all(2, 3, 4))

def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_tags(name="Pinky", age=21, city="Hyderabad")

def describe_person(name, *hobbies):
    print("Name:", name)
    print("Hobbies:", hobbies)

describe_person("Pinky", "Reading", "Coding", "Music")

def f(*args):
    print(type(args))

f(1, 2, 3)

def create_html_tag(tag, **attributes):

    print(f"<{tag}", end=" ")

    for key, value in attributes.items():
        print(f"{key}='{value}'", end=" ")

    print(">")

def mixed(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

mixed(
    10,
    20,
    30,
    40,
    50,
    name="Pinky",
    city="Hyderabad"
)

def demo(a, b, c=10, *args, **kwargs):
    pass

#functional reference
count = len

numbers = [10, 20, 30, 40, 50]

print(count(numbers))

def square(x):
    return x * x

def run_twice(func, value):
    return func(func(value))

print(run_twice(square, 2))

text = "hello python"

operations = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title
}

choice = "title"

print(operations[choice](text))

def make_multiplier(n):

    def multiply(x):
        return x * n

    return multiply

times3 = make_multiplier(3)

print(times3(10))

def greet():
    print("Hello")

functions = {
    "hello": greet,
    "hi": greet,
    "welcome": greet
}

functions["hello"]()
functions["hi"]()
functions["welcome"]()
#lambda
cube = lambda x: x ** 3

print(cube(3))

largest = lambda x, y: x if x > y else y

print(largest(10, 20))

#regular form
def even(n):
    return n % 2 == 0

even = lambda n: n % 2 == 0

print(even(8))
print(even(7))
items = [
    (1, 'banana'),
    (2, 'apple'),
    (3, 'cherry')
]
items.sort(key=lambda x: x[1])

print(items)
def square(n):
    return n * n

result = lambda x: square(x)

print(result(5))

def greet(name):
    return "Hello " + name

msg = lambda name: greet(name)

print(msg("Pinky"))


#high order functions
celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)
words = ["Apple", "banana", "Cat", "dog", "Elephant"]

result = list(filter(lambda word: word[0].isupper(), words))

print(result)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)

people = [
    ("Pinky", 21),
    ("Ravi", 25),
    ("Anu", 19)
]

result = sorted(
    people,
    key=lambda x: x[1],
    reverse=True
)

print(result)

numbers = range(1, 11)

evens = filter(lambda x: x % 2 == 0, numbers)

result = list(map(lambda x: x * x, evens))

print(result)
def my_map(func, lst):

    result = []

    for item in lst:
        result.append(func(item))

    return result


numbers = [1, 2, 3, 4]

print(my_map(lambda x: x * 2, numbers))

from functools import reduce

words = [
    'cat',
    'elephant',
    'dog',
    'rhinoceros'
]

result = reduce(
    lambda x, y: x if len(x) > len(y) else y,
    words
)

print(result)