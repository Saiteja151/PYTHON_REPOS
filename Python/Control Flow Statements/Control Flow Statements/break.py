"""
    Python break Statement
        The break statement is used to terminate the loop immediately when it is encountered.

        The syntax of the break statement is:
             break
"""


""" 
    Python break Statement with for Loop
        We can use the break statement with the for loop to terminate the loop when a certain condition is met. 
"""

for i in range(5):
    if i == 3:
        break

    print(i)

"""
Output:
        0
        1
        2
"""

print()


cart = [10, 20, 600, 60, 70]

for item in cart:
    if item > 500:
        print("To place this order insurance must be required")
        break

    print(item)

"""
Output:
        10
        20
        To place this order insurance must be required
"""

print()


""" 
    Python break Statement with while Loop
        We can also terminate the while loop using the break statement. 
"""

# program to find the first 5 multiples of 6

i = 1

while i <= 10:
    print("6 *", i, "=", 6 * i)

    if i >= 5:
        break

    i = i + 1

"""
Output:
        6 * 1 = 6
        6 * 2 = 12
        6 * 3 = 18
        6 * 4 = 24
        6 * 5 = 30
"""

print()
