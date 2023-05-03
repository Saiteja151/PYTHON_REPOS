"""
    Python if...else Statement
         In Python, there are three forms of the if...else statement.

           1) if statement
           2) if...else statement
           3) if...elif...else statement
"""

"""  
    1. Python if statement
        The syntax of if statement in Python is:
            if condition:
                # body of if statement
"""

number = 10

# check if number is greater than 0
if number > 0:
    print("Number is positive")

print("If statement is easy")

""" 
Output :
      Number is positive
      If statement is easy
"""

print()

number = -5

# check if number is greater than 0
if number > 0:
    print("Number is positive")

print("If statement is easy")

""" 
Output :
      If statement is easy
"""

print()


""" 
    2. Python if...else Statement
        An if statement can have an optional else clause.
        The syntax of if...else statement is:
                if condition:
                    # block of code if condition is True
                else:
                    # block of code if condition is False
"""

number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative number")

print("The statement is always executed")

""" 
Output :
      Positive number
      The statement is always executed
"""

print()

number = -5

if number > 0:
    print("Positive number")
else:
    print("Negative number")

print("The statement is always executed")

""" 
Output :
      Negative number
      The statement is always executed
"""

print()

""" 
    3. Python if...elif...else Statement
        The if...else statement is used to execute a block of code among two alternatives.
        
        However, if we need to make a choice between more than two alternatives, 
        then we use the if...elif...else statement.
        
        The syntax of if...elif...else statement is:
                if condition1:
                    # code block 1
                elif condition2:
                    # code block 2
                else:
                    # code block 3                  
"""

number = int(input("Enter a number :"))

if number > 0:
    print("Positive number")

elif number == 0:
    print("Zero")

else:
    print("Negative number")

print("This statement is always executed")


""" 
Output :
      Enter a number :0
      Zero
      This statement is always executed
"""

print()

""" 
    3. Python Nested if Statement
        We can also use an if statement inside of an if statement. This is known as a nested if statement.

        The syntax of nested if statement is:
                
                # outer if statement
                if condition1:
                    # statement(s)
                
                    # inner if statement
                    if condition2:
                        # statement(s)                
"""

number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
        print("Number is 0")

    # inner else statement
    else:
        print("Number is positive")

# outer else statement
else:
    print("Number is negative")

"""
Output:
    Number is positive
"""
