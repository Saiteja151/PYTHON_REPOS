""" A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
The parentheses are optional, however, it is a good practice to use them.
A tuple can have any number of items, and they may be of different types (integer, float, list, string, etc.)."""

# we can also create tuples without using parentheses ( The parentheses are optional )
t = 10, 20, 30, 40
print(t)     # (10, 20, 30, 40)

# Empty tuple
my_tuple = ()
print(my_tuple)     # ()

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)     # (1, 2, 3)

# tuple having mixed datatypes
my_tuple = (1, "Hello", 3.6)
print(my_tuple)     # (1, "Hello", 3.6)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)     # ('mouse', [8, 4, 6], (1, 2, 3))

print()

"""

    Create a Python Tuple With one Element
    In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.

    We will need a trailing comma to indicate that it is a tuple,

"""

# We can use the type() function to know which class a variable or a value belongs to.

var1 = ("Hello")
print(type(var1))      # <class 'str'>

var2 = ("Hello",)
print(type(var2))      # <class 'tuple'>

var3 = "Hello",
print(type(var3))      # <class 'tuple'>

print()

""" Access Python Tuple Elements """

"""
    1. Indexing
        We can use the index operator [] to access an item in a tuple, where the index starts from 0.
        So, a tuple having 6 elements will have indices from 0 to 5.
        Trying to access an index outside of the tuple index range( 6,7,... in this example) will raise an IndexError.
"""

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(len(letters))      # 9

print()

print(letters[0])      # p
print(letters[6])      # m
print(letters[5])      # a
print(letters[2])      # 0

print()

"""
    2. Negative Indexing
            Python allows negative indexing for its sequences.
            The index of -1 refers to the last item, -2 to the second last item and so on. 
"""

# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-9])      # p
print(letters[-7])      # 0
print(letters[-1])      # z

print()

"""
    3. Slicing
       We can access a range of items in a tuple by using the slicing operator colon :
"""

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])        # ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7])        # ('p', 'r')

# elements 8th to end
print(my_tuple[7:])        # ('i', 'z')

# elements beginning to end
print(my_tuple[:])        # ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print()


"""
    Python Tuple Methods
        In Python ,methods that add items or remove items are not available with tuple.
        Only the following two methods are available.
"""

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))     # 2
print(my_tuple.index('l'))     # 3


print()


"""
    Iterating through a Tuple in Python
        We can use the for loop to iterate over the elements of a tuple.
"""

languages = ('Python', 'Swift', 'C++')

# iterating through the tuple
for language in languages:
    print(language)

"""
output:
        Python
        Swift
        C++
"""

print()

"""
    Check if an Item Exists in the Python Tuple
        We use the in keyword to check if an item exists in the tuple or not. 
"""

languages = ('Python', 'Swift', 'C++')

print('C' in languages)    # False
print('Python' in languages)    # True
