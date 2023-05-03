# global variable
c = 1


def add():
    print(c)


add()

print()

""" 
# global variable
c = 1


def add():

    # increment c by 2
    c = c + 2

    print(c)


add()
"""

""" Example: Changing Global Variable From Inside a Function using global """

# global variable
c = 1


def add():

    # use of global variable
    global c

    # increment c by 2
    c = c + 2

    print(c)


add()

print()

""" Global in Nested Functions """


def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

    print("Before calling inner_function :", num)
    inner_function()
    print("After calling outer_function :", num)


outer_function()
print("Outside both function :", num)
