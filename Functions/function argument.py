""" Example 1: Python Function Arguments """


def add_numbers(a, b):
    total = a + b
    print("Sum :", total)


add_numbers(5, 9)

print()

""" Function Argument with Default Values """


def add_numbers(a=7, b=8):
    total = a + b
    print("Sum :", total)


# function call with two arguments
add_numbers(2, 3)


# function call with one argument
add_numbers(a=2)


# function call with no arguments
add_numbers()

print()


""" Python Keyword Argument """


def display_info(first_name, last_name):
    print("First Name :", first_name)
    print("Last Name :", last_name)


# function call
display_info("Sai", "Teja")


# function call
display_info(last_name="Cartman", first_name="Eric")

print()


""" Python Function With Arbitrary Arguments """


# program to find sum of multiple numbers
def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    print("Sum :", result)


# function call with three arguments
find_sum(1, 2, 3)


# function call with two arguments
find_sum(4, 9)
