# Newline is backslash n --->\n
print("Hello World!")
print(1+2)
print(10*3)
print(10*3.5)
print()

# Prints outputs in different lines
print("PrepInsta")
print("is")
print("best")

# Blank line
print()

# Prints outputs in same line
print("PrepInsta is best")

print()

# Prints outputs in same line
print("PrepInsta", "is", "best", "website")
print("PrepInsta", "is", "best", "website", 5)

print()

# Understanding the seperator in print function
# By default seperator value is empty space
print("PrepInsta", "is", "best", "website")
print("PrepInsta", "is", "best", "website", sep="")

# We can also give no space as a seperator
print("PrepInsta", "is", "best", "website", sep="")

print()

# After each and every coma separated values we can insert seperator
print("PrepInsta", "is", "best", "website", sep="_")
print("PrepInsta", "is", "best", "website", sep='@')
print("PrepInsta", "is", "best", "website", sep="+")
print("PrepInsta", "is", "best", "website", sep="%")
print("PrepInsta", "is", "best", "website", sep="__%__")

print()

# Understanding the end in print function
# By default end value is newline -->\n
print("PrepInsta", "is", "best", "website", end="")
print("mickey", "mouse")

print()

print("PrepInsta", "is", "best", "website", end="")
print("mickey", "mouse")

print()

print("PrepInsta", "is", "best", "website")
print("mickey", "mouse")

print()

print("PrepInsta", "is", "best", "website", end="\n")
print("mickey", "mouse")

print()

# By using end we can specify what to print at the end of the line
print("PrepInsta", "is", "best", "website", end="@@")
print("mickey", "mouse")

print()

# Using value,seperator,end in print function
print("PrepInsta", "is", "best", "website", sep="_", end="@@\n")
print("NewLine")
