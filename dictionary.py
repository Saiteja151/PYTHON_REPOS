"""

    Python dictionary is an ordered collection (starting from Python 3.7) of items.
It stores elements in key/value pairs.
Here, keys are unique identifiers that are associated with each value.

    Syntax :
            d = {key: value, key: value}

"""

capital_city = {"Nepal": "Kathmandu", "Sikkim": "Gangtok", "Italy": "Rome", "England": "London"}
print(capital_city)     # {'Nepal': 'Kathmandu', 'Sikkim': 'Gangtok', 'Italy': 'Rome', 'England': 'London'}

print()

""" Example 1: Python Dictionary """

# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)     # {1: 'One', 2: 'Two', 3: 'Three'}

print()

""" Add Elements to a Python Dictionary """

capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ", capital_city)      # {'Nepal': 'Kathmandu', 'England': 'London'}

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ", capital_city)      # {'Nepal': 'Kathmandu', 'England': 'London', 'Japan': 'Tokyo'}

print()

""" Change Value of Dictionary """

student_id = {111: "Kyle", 112: "Eric", 113: "Butters"}
print("Initial Dictionary: ", student_id)       # {111: 'Kyle', 112: 'Eric', 113: 'Butters'}

student_id[112] = "Stan"

print("Updated Dictionary: ", student_id)       # {111: 'Kyle', 112: 'Stan', 113: 'Butters'}

print()


""" Accessing Elements from Dictionary """

student_id = {111: "Kyle", 112: "Eric", 113: "Butters"}

print(student_id[111])         # Kyle
print(student_id[112])         # Eric
print(student_id[113])         # Butters

""" KeyError """

# student_id = {111: "Kyle", 112: "Eric", 113: "Butters"}

# print(student_id[211])

# KeyError: 211

print()

""" Removing elements from Dictionary """

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print("Initial Dictionary: ", student_id)         # {111: 'Eric', 112: 'Kyle', 113: 'Butters'}

del student_id[111]

print("Updated Dictionary: ", student_id)         # {112: 'Kyle', 113: 'Butters'}


""" We can also delete the whole dictionary using the del statement """

# student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

# delete student_id dictionary
# del student_id

# print(student_id)

# Output: NameError: name 'student_id' is not defined

print()


""" Dictionary Membership Test """

# Membership test for dictionary keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output : True
print(1 in squares)       # True

print(2 not in squares)       # True

# membership tests for key only not value
print(49 in squares)       # False

print()


""" Iterating Through a Dictionary """

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

for i in squares:
    print(squares[i])

"""
    Output:
            1
            9
            25
            49
            81
"""