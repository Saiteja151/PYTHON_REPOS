"""
    A set can have any number of items, and they may be of different types (integer, float, tuple, string etc.).

    But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

    Sets are unordered because we cannot get the same output everytime when we execute.

    Sets are an unordered collection of unique elements, which means that they cannot have duplicate elements.
"""

# create a set of integer type
student_id = {120, 112, 114, 116, 118}

print("Student ID:", student_id)       # {112, 114, 116, 118, 120}
print(type(student_id))       # <class 'set'>

print()

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}

print('Vowel Letters:', vowel_letters)       # {'a', 'i', 'o', 'e', 'u'}
print(type(vowel_letters))       # <class 'set'>

print()

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}

print('Set of mixed data types:', mixed_set)       # {'Hello', 'Bye', 101, -2}      # {'Bye', 101, 'Hello', -2}
print(type(mixed_set))       # <class 'set'>

"""

This Python code creates a set called mixed_set which contains four elements of different data types: 
    a string 'Hello', an integer 101, a negative integer -2, and another string 'Bye'.
    
The output of print('Set of mixed data types:', mixed_set) will display the set of mixed data types as follows:
Set of mixed data types: {'Bye', 'Hello', 101, -2}

Sets are an unordered collection of unique elements, which means that they cannot have duplicate elements.

In this case, the set mixed_set contains four unique elements, even though they are of different data types.

Note that sets are created using curly braces {} or the set() constructor, and elements are separated by commas.

"""

print()


"""
    
    Create an Empty Set in Python
            Note that sets are created using curly braces {} or the set() constructor, 
            and elements are separated by commas.
            
            To make a set without any elements, we use the set() function without any argument.

"""

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty set
print("Data type of empty_set:", type(empty_set))          # <class 'set'>

# check data type of empty dictionary
print("Data type of empty_dictionary:", type(empty_dictionary))          # <class 'dict'>

print()


""" Duplicate Items in a Set """
numbers = {2, 4, 6, 6, 2, 8}

print(numbers)         # {8, 2, 4, 6}

print()

""" Add and Update Set Items in Python """

# Add Items to a Set in Python
numbers = {21, 33, 54, 12}

print("Initial Set:", numbers)         # {33, 12, 21, 54}

# Using add() method
numbers.add(32)

print("Updated Set:", numbers)         # {32, 33, 12, 21, 54}

print()

""" Update Python Set """

companies = {'capgemini', 'cognizant'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)         # {'apple', 'cognizant', 'google', 'capgemini'}

print()

""" Remove an Element from a Set """

languages = {'Swift', 'Java', 'Python'}

print("Initial Set:", languages)        # {'Python', 'Java', 'Swift'}

# remove java from set

removed_value = languages.discard('Java')

print("Set after remove():", languages)        # {'Python', 'Swift'}

print()

""" Iterate Over a Set in Python """

fruits = {'Apple', 'Peach', 'Mango'}

# for loop to access each fruit
for fruit in fruits:
    print(fruit)

""" 
    Output:
            Peach
            Mango
            Apple
"""

print()

""" Find Number of Set Elements """

even_numbers = {2, 4, 6, 8}
print("Set:", even_numbers)        # {8, 2, 4, 6}

print("Total no of elements:", len(even_numbers))          # 4

print()


""" Python Set Operations """

""" 
    
    Union of Two Sets
        The union of two sets A and B include all the elements of set A and B.
        We use the | operator or the union() method to perform the set union operation.
"""

# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print("Union using | :", A | B)        # {0, 1, 2, 3, 4, 5}

# perform union operation using union()
print("Union using union():", A.union(B))        # {0, 1, 2, 3, 4, 5}

print()


""" 

    Set Intersection
        The intersection of two sets A and B include the common elements between set A and B.
        In Python, we use the & operator or the intersection() method to perform the set intersection operation.
"""

# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using | :', A & B)        # {1, 3}

# perform intersection operation using intersection()
print('Intersection using intersection() :', A.intersection(B))        # {1, 3}

print()


"""
    Difference between Two Sets
        The difference between two sets A and B include elements of set A that are not present on set B.
        We use the - operator or the difference() method to perform the difference between two sets.
"""

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using -
print("Difference using - :", A - B)        # {3, 5}

# perform difference operation using difference()
print("Difference using difference() :", A.difference(B))        # {3, 5}

print()


""" 
    
    Set Symmetric Difference
        The symmetric difference between two sets A and B includes all elements of A and B 
        without the common elements.
        
        In Python, we use the ^ operator or the symmetric_difference() method to perform
        symmetric difference between two sets.

"""

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform Set Symmetric Difference using ^
print("Set Symmetric Difference using ^ :", A ^ B)         # {1, 3, 5, 6}

# perform Set Symmetric Difference using symmetric_difference()
print("Set Symmetric Difference using symmetric_difference() :", A.symmetric_difference(B))         # {1, 3, 5, 6}

print()


"""
    Check if two sets are equal
        We can use the == operator to check whether two sets are equal or not. 
"""

# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')

"""

Output: 
    Set A and Set B are equal

"""
