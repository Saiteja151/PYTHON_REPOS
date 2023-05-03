""" Python Multiple Inheritance """

""" 
Syntax:
        class SuperClass1:
            # features of SuperClass1
            
        class SuperClass2:
            # features of SuperClass2
            
        class MultiDerived(SuperClass1, SuperClass2):
            # features of SuperClass1 + SuperClass2 + MultiDerived class
"""

""" Example: Python Multiple Inheritance """


class Mammal:
    def mammal_info(self):
        print("Mammals can give birth")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap")


class Bat(Mammal, WingedAnimal):
    pass


# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()

"""
Output:
        Mammals can give direct birth.
        Winged animals can flap.
"""

print()

""" Python Multilevel Inheritance """

"""
Syntax:
        class SuperClass:
            # Super class code here
            
        class DerivedClass1(SuperClass):
            # Derived class 1 code here
            
        class DerivedClass2(DerivedClass1):
            # Derived class 2 code here
"""

""" Example: Python Multilevel Inheritance """


class SuperClass:

    def super_method(self):
        print("Super class method called")


# define class that derive from SuperClass
class DerivedClass1(SuperClass):

    def derived1_method(self):
        print("Derived class 1 method called")


# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()

d2.derived1_method()

d2.derived2_method()

"""
Output:
        Super class method called
        Derived class 1 method called
        Derived class 2 method called
"""

print()

""" Method Resolution Order (MRO) in Python """


class SuperClass1:
    def info(self):
        print("Super Class 1 method called")


class SuperClass2:
    def info(self):
        print("Super Class 2 method called")


class Derived(SuperClass1, SuperClass2):
    pass


d1 = Derived()
d1.info()

"""
Output:
        Super Class 1 method called
"""
