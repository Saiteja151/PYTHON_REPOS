""" A list is created in Python by placing items inside [], separated by commas . """
# We can also create empty list
List = []
print(List)         # []
print(type(List))       # <class 'list'>

print()

# list can take same datatypes
# Creating a list containing 3 integers
numbers = [1, 2, 3]
print(numbers)       # [1, 2, 3]
print(type(numbers))    # <class 'list'>

print()

# list can take different datatypes or mixed datatypes
mixed_list = [1, "Hello", 5.5]
print(mixed_list)       # [1, 'Hello', 5.5]
print(type(mixed_list))     # <class 'list'>

print()

""" 
    Accessing elements of a list
    1. Accessing elements of a list using index
    2. Accessing elements of a list using slice operator(:) 
"""

# 1. Accessing elements of a list using index
subjects = ["Physics", "Chemistry", "Maths"]

# List support positive indexing
print(subjects[0])         # Physics
print(subjects[1])         # Chemistry
print(subjects[2])         # Maths

print()

# List support negative indexing
print(subjects[-3])         # Physics
print(subjects[-2])         # Chemistry
print(subjects[-1])         # Maths

print()

# Throws error when list index is out of range
# print(subjects[5])

""" 
    2. Accessing elements of a list using slice operator(:)
    list2 = list1[start:stop:step] 
    start => default value is 0
    stop  => maximum allowed length of list
    step  => increment value. default value is 1
    
    In Python it is possible to access a section of items from the list using the slicing operator :, 
    not just a single item.
"""

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# items from index 2 to index 4
print(my_list[2:5])         # ['o', 'g', 'r']

# items from index 5 to end
print(my_list[5:])         # ['a', 'm', 'i', 'z']

# items beginning to end
print(my_list[:])         # ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

print()

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# items from index 2 to index 6 and having increment value = 2
print(my_list1[2:7:2])          # [3, 5, 7]

# items from index 4 to end and having increment value = 2
print(my_list1[4::2])          # [5, 7, 9]

""" 
In the given code, my_list1 is a list of 10 integers, and the slice operation my_list1[4:100] is performed on it. 
Since the end_index is 100 which is greater than the length of the list, 
Python simply returns all the elements from the start_index (i.e. 4) to the end of the list.
So, the output of the code will be a list containing elements from index 4 
to the end of the list which are [5, 6, 7, 8, 9, 10].
"""
print(my_list1[4:100])          # [5, 6, 7, 8, 9, 10]

print()

""" 
    Manipulating elements of list
    
    1. Adding elements to the list
        i) append --> a) Adding elements to a list 
                      b) Adding list to list
                      
        ii) extend --> a) Using extend
                       b) Add Elements of Tuple and Set to List
                       
        iii) insert --> a) Inserting an Element to the List
                        b) Inserting a Tuple (as an Element) to the List
    
        
    2. Remove an Item From a List
        i) delete
        
        ii) remove --> a) remove element from the list
                       b) remove() method on a list having duplicate elements
                       c) Deleting element that doesn't exist
    
        iii) pop --> a) pop item at the given index from the list
                     b) pop() without an index, and for negative indices
        
"""


""" 
1. Adding elements to the list
   i) append - The append() method adds an item at the end of the list.
               a) Adding elements to a list 
"""

animals = []

print("Before Append", animals)        # []

animals.append("cat")
animals.append("dog")
animals.append("fox")

print("After Append", animals)        # ['cat', 'dog', 'fox']

print()

letters = ['k', 'p', 'l', 'm', 'n']

print("Before Append", letters)       # ['k', 'p', 'l', 'm', 'n']

# using append method
letters.append(9)

print("After Append", letters)       # ['k', 'p', 'l', 'm', 'n', 9]

print()


""" 
1. Adding elements to the list
   i) append - The append() method adds a new list at the end of the list.
               b) Adding list to list
"""

# Animals list
Animals = ["cat", "dog", "rabbit"]

# wild_animals list
wild_animals = ["tiger", "fox"]

# appending wild_animals list to Animals
Animals.append(wild_animals)

print("Updated Animals list : ", Animals)       # ['cat', 'dog', 'rabbit', ['tiger', 'fox']]

wild_animals.append(Animals)

print("Updated Animals list : ", wild_animals)         # ["tiger", "fox", ['cat', 'dog', 'rabbit', ['tiger', 'fox']]]

print()


""" 
1. Adding elements to the list
    ii) extend --> a) Using extend
                    We use the extend() method to add all items of one list to another. 
"""

"""
    In this code, the order list contains three elements: "Chicken", "Mutton", and "Fish".
    The extend() method is used to add elements to the end of a list, and it takes an iterable as its argument. 
    In this case, the argument passed to extend() is the string "Mushroom".
    However, since a string is iterable, the extend() method treats each character in the string as an 
    individual element and adds them to the list.
    So, instead of adding the string "Mushroom" as a single element, 
    it adds each character in the string as a separate element.
    Therefore, the resulting order list will 
    contain seven elements: "Chicken", "Mutton", "Fish", "M", "u", "s", "h", "r", "o", "o", "m".
    So the output of the code will be:
    ['Chicken', 'Mutton', 'Fish', 'M', 'u', 's', 'h', 'r', 'o', 'o', 'm']
"""

order = ["Chicken", "Mutton", "Fish"]

order.extend("Mushroom")

print(order)       # ['Chicken', 'Mutton', 'Fish', 'M', 'u', 's', 'h', 'r', 'o', 'o', 'm']

print()

languages_1 = ["French", "English"]

languages_2 = ["Spanish", "Portuguese"]

languages_1.extend(languages_2)

print('Language list:', languages_1)        # ['French', 'English', 'Spanish', 'Portuguese']

print()

""" 
1. Adding elements to the list
    ii) extend --> b) Add Elements of Tuple and Set to List 
"""

# languages list
languages = ["French"]

# languages tuple
languages_tuple = ("Spanish", "Portuguese")

# languages set
languages_set = {"Chinese", "Japanese"}

# appending languages_tuple to languages
languages.extend(languages_tuple)

print("New language list: ", languages)        # ['French', 'Spanish', 'Portuguese']

# appending languages_set to languages
languages.extend(languages_set)

print("New language list: ", languages)        # ['French', 'Spanish', 'Portuguese', 'Japanese', 'Chinese']

print()

""" 
1. Adding elements to the list
    ii) insert --> a) Inserting an Element to the List
    
                        The insert() method inserts an element to the list at the specified index.
                        The syntax of the insert() method is
                                list.insert(i, elem)
                                Here, elem is inserted to the list at the ith index. 
                                All the elements after elem are shifted to the right.
                        
                        The insert() method takes two parameters:
                                index - the index where the element needs to be inserted
                                element - this is the element to be inserted in the list
                                
                        Notes:
                                If index is 0, the element is inserted at the beginning of the list.
                                If index is 3, the index of the inserted element will be 3 (4th element in the list).                             
"""

# Creates list of prime numbers
prime_numbers = [2, 3, 5, 7]

# insert 11 at index 4
prime_numbers.insert(4, 11)

print("List : ", prime_numbers)       # [2, 3, 5, 7, 11]

print()

""" 
1. Adding elements to the list
    ii) insert --> b) Inserting a Tuple (as an Element) to the List                      
"""

mixed_list_1 = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list_1.insert(1, number_tuple)

print("Updated list :", mixed_list_1)      # [{1, 2}, (3, 4), [5, 6, 7]]

print()

"""
2. Remove an Item From a List
        i) delete - In Python we can use the del statement to remove one or more items from a list.
"""

languages_3 = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages_3[1]         # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
print(languages_3)

# deleting the last item
del languages_3[-1]        # ['Python', 'C++', 'C', 'Java', 'Rust']
print(languages_3)

# delete first two items
del languages_3[0:2]       # ['C', 'Java', 'Rust']
print(languages_3)

print()


"""
2. Remove an Item From a List
        ii) remove - a) remove element from the list.
                        The remove() method removes the first matching element 
                        (which is passed as an argument) from the list.
                        
                        Syntax of List remove() : 
                                        The syntax of the remove() method is:
                                                list.remove(element)
                                                
                                        remove() Parameters
                                            The remove() method takes a single element as an argument 
                                            and removes it from the list.
                                            If the element doesn't exist, 
                                                it throws ValueError: list.remove(x): x not in list exception.
                                            
                                        Return Value from remove()
                                            The remove() doesn't return any value (returns None).
"""

# creates a list
Prime_Numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from list
Prime_Numbers.remove(9)

# Updated Prime_Numbers list
print(Prime_Numbers)        # [2, 3, 5, 7, 11]

print()

""" 
2. Remove an Item From a List
        ii) remove - b) remove() method on a list having duplicate elements.
                        If a list contains duplicate elements, the remove() method only 
                        removes the first matching element.
"""

# fruits list
fruits = ["banana", "apple", "apple", "mango", "papaya"]

# remove apple from the list
fruits.remove("apple")

# updated fruits list
print("Updated fruits list: ", fruits)      # ['banana', 'apple', 'mango', 'papaya']

print()


""" 
2. Remove an Item From a List
        ii) remove - c) Deleting element that doesn't exist
"""

# flowers list
# flowers = ["rose", "jasmine", "lily", "sunflower"]

# deleting dahlia from list
# flowers.remove("dahlia")

# Updated flowers list
# print("Updated flowers list: ", flowers)

"""
Output :
Traceback (most recent call last):
  File ......... , line 364, in <module>
    flowers.remove("dahlia")
ValueError: list.remove(x): x not in list
"""

print()

"""
2. Remove an Item From a List
        iii) pop - a) pop item at the given index from the list
                      The pop() method removes the item at the given index from the list and returns the removed item.
                      
                      Syntax of List pop()
                        The syntax of the pop() method is:
                        list.pop(index)
                        
                      pop() parameters
                        The pop() method takes a single argument (index).
                        The argument passed to the method is optional.
                        If not passed, the default index -1 is passed as an argument (index of the last item).
                        If the index passed to the method is not in range, 
                        it throws IndexError: pop index out of range exception.  
                      
                     Return Value from pop()
                       The pop() method returns the item present at the given index.
                       This item is also removed from the list.                      
"""

# emotions list
emotions = ["happy", "sad", "angry", "fear", "surprise"]

# remove and return the 4th item
return_value = emotions.pop(3)
print("Return value: ", return_value)       # Return value:  fear

# Updated list
print("Updated list: ", emotions)           # Updated List: ['happy', 'sad', 'angry', 'surprise']

print()

"""
2. Remove an Item From a List
        iii) pop - b) pop() without an index, and for negative indices
"""

# vegetables list
vegetables = ["tomato", "potato", "carrot", "onion", "cabbage"]

# remove and return the last item
print("When index is not passed:")
print("Return value: ", vegetables.pop())       # cabbage
print("Updated list: ", vegetables)             # ['tomato', 'potato', 'carrot', 'onion']

# remove and return the last item
print("\nWhen -1 is passed:")
print("Return value: ", vegetables.pop(-1))      # onion
print("Updated list: ", vegetables)              # ['tomato', 'potato', 'carrot']

# remove and return the third last item
print("\nWhen -3 is passed:")
print("Return value: ", vegetables.pop(-3))      # tomato
print("Updated list: ", vegetables)              # ['potato', 'carrot']

print()


""" Iterating through a List """

flowers = ["rose", "jasmine", "lily"]

# Iterating over list
for flower in flowers:
    print(flower)

"""
output:
        rose
        jasmine
        lily
"""

""" Python List Length """

languages_4 = ['Python', 'Swift', 'C++']

print("\nList: ", languages_4)      # ['Python', 'Swift', 'C++']

print("Total Elements: ", len(languages_4))     # 3

print()

""" Python List Comprehension """

s = [x*x for x in range(1, 11)]
print(s)        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

m = [2**x for x in range(1, 6)]
print(m)        # [2, 4, 8, 16, 32]
