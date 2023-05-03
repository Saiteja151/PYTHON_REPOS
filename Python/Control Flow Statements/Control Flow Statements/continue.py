"""
    Python continue Statement with for Loop
        We can use the continue statement with the for loop to skip the current iteration of the loop.
        Then the control of the program jumps to the next iteration.
"""

for i in range(5):
    if i == 3:
        continue

    print(i)

"""
Output:
        0
        1
        2
        4
"""

print()


""" To print odd numbers in the range 0 to 9 """

for i in range(10):
    if i % 2 == 0:
        continue

    print(i)

"""
Output:
        1
        3
        5
        7
        9
"""

print()


cart = [10, 20, 500, 700, 50, 60]

for item in cart:
    if item >= 500:
        print("We cannot process this item :", item)
        continue

    print(item)

"""
Output:
        10
        20
        We cannot process this item : 500
        We cannot process this item : 700
        50
        60
"""

print()


numbers = [10, 20, 0, 5, 0, 30]

for n in numbers:
    if n == 0:
        print("Hey how we can divide with zero..just skipping")
        continue

    print("100/{} = {}".format(n, 100/n))


"""
Output:
        100/10 = 10.0
        100/20 = 5.0
        Hey how we can divide with zero..just skipping
        100/5 = 20.0
        Hey how we can divide with zero..just skipping
        100/30 = 3.3333333333333335
"""

print()


""" 
    Python continue Statement with while Loop
        In Python, we can also skip the current iteration of the while loop using the continue statement. 
"""

# program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1

    if (num % 2) == 0:
        continue

    print(num)

"""
Output:
        1
        3
        5
        7
        9
"""
