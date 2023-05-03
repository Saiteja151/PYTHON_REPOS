""" Classes & Objects """

""" 
    Class 
    syntax:  
        class ClassName:
            # class Definition
"""

"""
    Objects
    syntax:
        objectName = ClassName()
"""

""" Example of object creation """


# create class
class Bike:
    name = ""
    gear = 0


# creating object of class
bike1 = Bike()

""" Access Class Attributes Using Objects """

# modify the name attribute
bike1.name = "Mountain Duke"

# access the gear attribute
bike1.gear

""" Example 1: Python Class and Objects """


# define a class
class Bike:
    name = ""
    gear = 0


# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear}")  # Name: Mountain Bike, Gears: 11

print()

""" Create Multiple Objects of Python Class """


# define class
class Employee:
    # define an attribute
    employee_id = 0


# create two objects of Employee class
employee1 = Employee()
employee2 = Employee()

# access attribute using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attribute using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")

"""
Output:
        Employee ID: 1001
        Employee ID: 1002
"""

print()

""" Python Method """


# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()

""" 
Output:
        Area of Room = 1309.0
"""

print()

""" Python Constructors """


class Bike:

    # constructor function
    def __int__(self, name=""):
        self.name = name


bike1 = Bike()
