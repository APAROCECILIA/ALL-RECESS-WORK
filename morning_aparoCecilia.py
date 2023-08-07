# Inheritence

# Assignment, circle and rectangle do inherit
# from shape class where we calculate the area and perimeter
# print("Assignment, circle and rectangle
# do inherit from shape class where we calculate the area and perimeter")

from abc import ABC, abstractmethod


class Shape:
    def calculate_area(self):
        pass


def calculate_perimeter(self):
    pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius

    def calculate_perimeter(self):
        return 2*self.radius*3.14


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width


def calculate_area(self):
    return self.length*self.width


def calculate_perimeter(self):
    return 2*(self.length + self.width)

# #create the objects of the child classes


circle = Circle(20)
rectangle = Rectangle(10, 30)

print("Area & Perimeter of circle:")
print(circle.calculate_area())
print(circle.calculate_perimeter())

print("Area & Perimeter of rectangle:")
print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())

# multiple inheritence


class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Material:
    def __init__(self, material):
        self.material = material

    def get_material(self):
        return self.material


class Square(Shape, Material):
    def __init__(self, side_length, color, material):
        Shape.__init__(self, color)
        Material.__init__(self, material)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length


# # Create an object of the Square class
square = Square(50, 'pink', 'metal')

# # Access methods from Shape class
print(square.get_color())

# # Access methods from Material class
print(square.get_material())

# # Access methods from Square class
print(square.calculate_area())


# #method overriding
print("........method overriding..........")


class Animal:
    def make_sound(self):
        print("animal makes sound")


class Dog(Animal):
    def make_sound(self):
        print("the dog made sound")


class Cat(Animal):
    def make_sound(self):
        print("the cat made sound")

    def sound_made(animal):
        animal.make_sound()


# the objects
animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()


# Polymorphism
# "polymorphism" means "many forms",
# and in programming it refers to methods/functions/operators
# with the same name that can be executed on many objects or classes.

# we shall do method overriding and method Overloading

class myAddition:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


# Using method overloading
calc = myAddition()
# print(calc.add(2, 3))       # This will raise an error because
# there's no method with two arguments
# print(calc.add(2, 3, 4))    # This will correctly call the add method with three arguments


# Abstraction
# It allows you to represent complex systems or
# entities in a simplified and understandable manner
# by hiding unnecessary details and exposing only relevant information
# we've picked a features from the abc class

print("ABSTRACTION CONCEPT")


class myClass(ABC):
    def open(self):
        pass

    def close(self):
        pass


class door(myClass):
    def open(self):
        print("open the door")

        def close(self):
            print("close the door")


class box(myClass):

    def open(self):
        print("open the box")

    def close(self):
        print("seal the box")


# #create the objects
door1 = door()
box1 = box()

print("for the door class")
door1.open()
door1.close()

print("for the box class")
box1.open()
box1.close()


# exercie
print("abstraction for area of the circle and rectangle demonstartion from the abc class")


class Shape(ABC):

    def calculate_area(self):
        pass

# the circle class inheriting from the abc class


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

# area of the circle is pi*r*r


def calculate_area(self):
    return 3.14*self.radius*self.radius

# the rectangle class inheriting from the abc class


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


def calculate_area(self):
    return self.length*self.width


# #the objects
circle = Circle(5)
rectangle = Rectangle(10, 5)

print(" The circle ;", circle.calculate_area())
print(" The rectangle", rectangle.calculate_area())
