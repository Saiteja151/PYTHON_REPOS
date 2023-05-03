""" Python Recursion """


def factorial(x):
    """ This is the recursive function to find the factorial of an integer """

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


num = 3
print("The factorial of", num, "is", factorial(num))

print()


def factorial(x):
    """ This is the recursive function to find the factorial of an integer """

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


num = int(input("Enter a number :"))
print("The factorial of", num, "is", factorial(num))
