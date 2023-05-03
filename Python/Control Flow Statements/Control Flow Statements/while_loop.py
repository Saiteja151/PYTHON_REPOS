""" Python while Loop
            Python while loop is used to run a block code until a certain condition is met.

            The syntax of while loop is:
                    while condition:
                         # body of while loop
"""

# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

"""
Output :
        1
        2
        3
        4
        5
"""

print()

# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input("Enter a number :"))

# adds numbers until the number is zero
while number != 0:
    total = total + number

    # take integer input again
    number = int(input("Enter a number :"))


print("Total =", total)

"""
Output :
        Enter a number :12
        Enter a number :-5
        Enter a number :4
        Enter a number :0
        Total = 11
"""

print()


""" Infinite while Loop in Python 

age = 32

# test condition is always true
while age > 18:
    print("You can vote")

"""


""" Python While loop with else """

counter = 0

while counter < 3:
    print("Inside Loop")
    counter = counter + 1
else:
    print("Inside else")


"""
Output :
        Inside Loop
        Inside Loop
        Inside Loop
        Inside else
"""

print()


""" The else block will not execute if the while loop is terminated by a break statement. """

counter = 0

while counter < 3:
    # loop ends because of break
    # else part is not executed
    if counter == 1:
        break

    print("Inside Loop")
    counter = counter + 1
else:
    print("Inside else")

"""
If number is equal to 1 loop breaks
If number is less than three 
        Output : Inside Loop
If number is greater than three
        Output : Inside else
"""

print()
