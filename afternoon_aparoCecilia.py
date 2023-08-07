# FUNCTIONS

import math as m
import mymodule_aparo


def Session():
    print("The afternoon session ends at 5:00 pm")


Session()


def hi(name):
    print(f"Hello, {name}! How are you today?")


hi("Aparo")  # call the function

# arguments; actual values assigned to the argument
# and parameters; variable,specified after the function name


def Student(name, age):
    print(F"Her name is: {name} and she is: {age} years old")


Student("Heavens", 50)


def add(a, b):
    return (a + b)


def product(a, b):
    return (a * b)


print(product(4, 6))

# MODULES
# accessing mymodule from another file

mymodule_aparo.sayHello("cecilia")

result = mymodule_aparo.add(3, 5)
print(result)

result = mymodule_aparo.multiply(13, 35)
print(result)


# USING alias,
# In Python, an alias refers to an alternative name given
# to a module, function, or class.
# It allows you to create a shorter or more convenient name to reference the original object
# For example


radius = 5
circumference = 2 * m.pi * radius
area = m.pi * m.pow(radius, 2)

print(f"Circumference: {circumference}")
print(f"Area: {area}")

'''USER INPUT
python 3.6 uses input() method
python 3.6 uses raw_input() method

this example takes in username
'''
username = input("Enter username: ")
print("username is: " + username)

# multiple inputs in python: use same data type
s, r, w = map(int, input("enter the  values : ").split())
print("The values  are : ", end=" ")

result = s, r, w
print(result)

# how to capture input from a tuple
w = (2, 3, 4, 5, 6)
print("current tuple")
print(w)
print(type(w))

E = list(w)
E.append(int(input("enter new values: ")))
w = tuple(E)
print("updated tuple")
print(w)

mylist = list(map(int, input("enter the list values : ").split()))
myset = set(map(int, input("enter the set values : ").split()))

print(mylist)
print(type(mylist))

print(myset)
print(type(myset))
