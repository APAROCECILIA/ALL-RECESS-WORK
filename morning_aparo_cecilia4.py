#  MORNING SESSION

'''classes $ objects and inheritance
'''


import math


class house:
    type = "flat"
    location = "muyenga"
    price = "USD10000"


H1 = house()
print(H1.location)
'''
above is the simplest form of a class and its object 
but each classhas a function __init__(), it is used to assgn values 
to object properties or initialise values of a class when an object 
of the class is being created'''

'''you can delete the above obove object by using the del keyword
 del h2
 
 for a class without content just add  a key word
 "pass" to avoid errors

the __str__() function controls what should be returned when the
object is represented as a string
'''


class house:
    def __init__(self, type, location, price):
        self.type = type
        self.location = location
        self.price = price

    def property(self):
        print("the property is at: " + self.location)


# instance of the class house
h2 = house("bangalo", "kololo", "USD1000")
print(h2.type)
print(h2.location)
print(h2.price)


# EXAMPLE OF A BANK ACCOUNT

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        else:
            print("insufficient funds")

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print("Account Number:" + self.account_number)
        print(f"Balance: {self.balance}")


my_account = BankAccount("123456789", 1000)
# operations of the class above;

my_account.display_balance()
my_account.deposit(300)
my_account.withdraw(200)
my_account.display_balance()


# class rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Creating an instance of Rectangle
rectangle = Rectangle(5, 3)

# Calculating the area
area = rectangle.area()
print(f"The area of the rectangle is: {area}")

# Calculating the perimeter
perimeter = rectangle.perimeter()
print(f"The perimeter of the rectangle is: {perimeter}")

# class circle ;find area and perimeter


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Creating an instance of Circle
circle = Circle(5)

# Calculating the area
area = circle.area()
print(f"The area of the circle is: {area:.2f}")

# Calculating the perimeter
perimeter = circle.perimeter()
print(f"The perimeter of the circle is: {perimeter:.2f}")


# ENCAPSULATION
'''
GOAL OF ENCAPSULATION
1.to hide the impletations
2.to protect the objects from changes
3.to protect the objects fron external changes
4.to protect the objects from code modularity
'''
# EXAMPLE: to demonstrate encapsulation


# conversion without the concept of encpsulation
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


celsius = 37
fahrenheight = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheight} degrees Fahrenheit.")


# show the concept of encapsulation; the underscore encapsulates the data

class TempConvert:
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        return (self._celsius * 1.8) + 32


# Creating an instance of TemperatureConverter
converter = TempConvert(37)

# Converting Celsius to Fahrenheit using encapsulated logic
fahrenheit = converter.to_fahrenheit()

print(f"The temperature in Fahrenheit is: {fahrenheit}°F")


# EXERCISE: calculate the employess salary with 0.15 bonus

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def bonus(self):
        bonus = 0.15 * self._salary
        salary_with_bonus = self._salary + bonus
        return salary_with_bonus


# Creating an instance of Employee
employee = Employee("APARO ", 1000000)

# Accessing attributes using encapsulated methods
name = employee.get_name()
salary = employee.get_salary()
print(f"Employee Name: {name}, Salary: {salary}")

# Calculating the salary with bonus using encapsulated method
salary_with_bonus = employee.bonus()
print(f"Salary with Bonus: {salary_with_bonus}")

# show encpsulation with employee information to give a pay incrementation
# (salary with employee information to new salary) eg. from 850,000 to 1000000


class CompanyEmployee:
    def __init__(self, name, profession, salary):
        self._name = name
        self._salary = salary
        self._profession = profession

    def get_name(self):
        return self._name

    def get_profession(self):
        return self._profession

    def get_salary(self):
        return self._salary

    def increment_salary(self, increment_amount):
        self._salary += increment_amount


# Creating an instance of Employee
employee = CompanyEmployee("Amario", "Frontend", 850000)

# Accessing attributes using encapsulated methods
name = employee.get_name()
salary = employee.get_salary()
profession = employee.get_profession()
print(f"Employee Name: {name},profession: {profession}, Salary: {salary} ")

# Incrementing the salary using encapsulated method
increment_amount = 150000
employee.increment_salary(increment_amount)

# Accessing the updated salary
updated_salary = employee.get_salary()
print(f"Updated Salary: {updated_salary}")


# inheritance,polymorphism and abstraction

# END OF MORNING SESSION
