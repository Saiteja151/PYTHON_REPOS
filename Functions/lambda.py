""" Python Lambda/Anonymous Function """

""" Example: Python lambda Function """

# declare a lambda function
greet = lambda: print("Hello World")

# lambda call
greet()

print()

""" Python lambda Function with an Argument """

# lambda that accepts one argument
greet_user = lambda name: print("Hey there,", name)

# lambda call
greet_user("Scooby")
# greet_user(input())       # taking input from user

print()

# lambda that accepts one argument
s = lambda n: n * n

print("The square of 4 is :", s(4))

print()

# lambda that accepts two arguments
s = lambda a, b: a + b

print("The sum of 10, 20 :", s(10, 20))

print()

# lambda that accepts three arguments
s = lambda a, b, c: a * b * c

print("Multiplication of a, b, c is :", s(11, 49, 57))

print()

# lambda function to find biggest of given values.
s = lambda a, b: a if a > b else b
print("The Biggest of 10, 20 is :", s(10, 20))
print("The Biggest of 100, 200 is :", s(100, 200))
