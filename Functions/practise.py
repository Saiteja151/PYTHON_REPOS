# function definition
def greet():
    print("Hello World!")


# function call
greet()

print("Outside of function")

print()


# function without return
def add_numbers(num1, num2):
    total = num1 + num2
    print("Sum :", total)


# function call
add_numbers(5, 6)
add_numbers(600, 1000)

print()


# function without return
def sub_numbers(num1, num2):
    sub = num1 - num2
    print("Sub :", sub)


# function call
sub_numbers(200, 100)
sub_numbers(95, 85)
sub_numbers(9.5, 4.5)
sub_numbers(4.5, 7.5)

print()


# function without return
def mul_numbers(num1, num2):
    mul = num1 * num2
    print("Mul :", mul)


# function call
mul_numbers(23, 33)
mul_numbers(45, 86)
mul_numbers(4.5, 58.33)

print()


# function without return
def div_numbers(num1, num2):
    div = num1 / num2          # Quotient
    div1 = num1 % num2         # Remainder
    print("Div :", div)
    print("Div :", div1)


# function call
div_numbers(4, 2)

print()


# function with return statement
def add_numbers(num1, num2):
    add = num1 + num2
    return add


# function call
ADD = add_numbers(3, 4)
print("Addition of two numbers :", ADD)

print()


# function with return statement
def sub_numbers(num1, num2):
    sub = num1 - num2
    return sub


# function call
SUB = sub_numbers(80, 9)
print("Subtraction of two numbers :", SUB)

print()


# function with return statement
def mul_numbers(num1, num2):
    mul = num1 * num2
    return mul


# function call
MUL = mul_numbers(50, 25)
print("Multiplication of two numbers :", MUL)

print()


# function with return statement
def div_numbers(num1, num2):
    div = num1 / num2
    return div


# function call
DIV = div_numbers(4, 2)
print("Division of two numbers(Quotient) :", DIV)

print()


# function with return statement
def div_numbers1(num1, num2):
    div = num1 % num2
    return div


# function call
Div = div_numbers1(50, 3)
print("Division of two numbers(Remainder) :", Div)
