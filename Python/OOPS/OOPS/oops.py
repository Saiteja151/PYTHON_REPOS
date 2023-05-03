""" Python Class and Object """


class Parrot:
    # class attribute
    name = ""
    age = 0


# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

""" 
Output:
        Blu is 10 years old
        Woo is 15 years old
"""

print()

""" Python Inheritance """


# base class
class Animal:

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")


# derived class
class Dog(Animal):

    def bark(self):
        print("I can bark! Woof woof!!")


# create object of Dog class
dog1 = Dog()

# calling members of base class
dog1.eat()
dog1.sleep()

# calling members of derived class
dog1.bark()

""" 
Output:
        I can eat!
        I can sleep!
        I can bark! Woof woof!!
"""

print()

""" Python Encapsulation """

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

"""
Output:
        Selling Price: 900
        Selling Price: 900
        Selling Price: 1000
"""

print()

""" Polymorphism """

class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square:
    # renders square
    def render(self):
        print("Rendering Square...")

class Circle:
    # renders circle
    def render(self):
        print("Rendering Circle...")

# create an object of Sqaure
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

""" 
Output:
        Rendering Square...
        Rendering Circle...
"""
