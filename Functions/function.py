""" Python Functions """

""" Python Function Declaration """


# The syntax to declare a function is:
def function_name(arguments):
    # function body

    return


""" 
    def - keyword used to declare function
    function_name - any name given to function
    arguments - any value passed to function
    return (optional) - returns value of the function
"""

""" Calling a Function in Python """


def greet():
    print("Hello World")


# function call
greet()

print()

""" Example: Python Function """


def greet():
    print("Hello World")


# function call
greet()
print("Outside the function")

print()

""" Example 1: Python Function Arguments """


# function with two arguments
def add_numbers(num1, num2):
    total = num1 + num2
    print("Sum :", total)


# function call with two values
add_numbers(5, 7)
add_numbers(20, 40)
add_numbers(100, 200)

print()


""" Example 2: Function return Type """


# function definition
def find_square(num):
    output = num * num
    return output


# function call
square = find_square(3)

print(square)

print()


""" Example 3: Add Two Numbers """


# function that adds two numbers
def add_numbers(num1, num2):
    total = num1 + num2
    return total


# function call
result = add_numbers(3, 5)
print("Sum :", result)

print()


""" Example 4: Python Library Function """
# we must include the module inside our program.
import math

# sqrt computes square root
square_root = math.sqrt(4)

print("Square root of 4 :", square_root)

# pow() computes power
power = pow(2, 3)

print(" 2 to the power 3 is", power)
