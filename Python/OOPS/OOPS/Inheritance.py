""" Python Inheritance """

""" 
    Syntax:
            # define a super class
            class super_class:
                # attributes and method definition
                
            # inheritance
            class sub_class(super_class):
                # attributes and method of super_class
                # attributes and method of sub_class
"""

""" Example 1: Python Inheritance """


class Animal:
    # attribute and method of parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of super class using self
        print("My name is ", self.name)


# create an object of subclass
labrador = Dog()

# access super class attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()

""" 
Output:
        I can eat
        My name is  Rohu
"""

print()

""" Example 2: Inheritance in Python """


class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()

"""
Output:
        Enter side 1 : 3
        Enter side 2 : 5
        Enter side 3 : 4
        Side 1 is 3.0
        Side 2 is 5.0
        Side 3 is 4.0
        The area of the triangle is 6.00
"""

print()


""" Method Overriding """


class Animal:
    # attributes and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")


# create an object of subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

"""
Output:
        I like to eat bones
"""

print()

""" The super() Method in Python Inheritance """


class Animal:
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        # call the eat() method of super class using super()
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()

"""
Output:
        I can eat
        I like to eat bones
"""
