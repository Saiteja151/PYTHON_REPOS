"""
    Python for Loop
        In Python, the for loop is used to run a block of code for a certain number of times.
        It is used to iterate over any sequences such as list, tuple, string, etc.

        The syntax of the for loop is:
            for val in sequence:
                # statement(s)

        Here, val accesses each item of sequence on each iteration.
        Loop continues until we reach the last item in the sequence.
"""

languages = ["Swift", "Python", "Go", "Javascript"]

# access items of a list using for loop
for language in languages:
    print(language)

print()

""" Python for Loop with Python range() """

# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)

""" 
Output:
        0
        1
        2
        3
"""

print()

""" Python for loop with else """

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left")

"""
Output:
        0
        1
        5
        No items left
"""
