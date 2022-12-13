#
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#

# Basic data types in Python: Numbers, Strings, Booleans,
# Sequences (such as Lists or Tuples), Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works
myint = "alpha"
# print(myint)

# to access a member of a sequence type, use []
# print(mylist[2])
# print(mytuple[1])

# use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[1:5:2])

# you can use slices to reverse a sequence
# print(mylist[::-1])

# dictionaries are accessed via keys
# print(mydict["one"])

# ERROR: variables of different types cannot be combined
#This produces a TypeError can only concatenate str (not "int") to str
# print("Good evening Pythoners " + 2361)
# print("Good evening Pythoners " + str(2361)) # Use type conversion

# Global vs. local variables in functions
def some_function():
    # To make this refer to the other variable use the keyword global with the variable name
    # global mystr
    mystr = "This is a local variable string"
    print(mystr)

some_function()
print(mystr)

del mystr # This deletes the variable and trying to access it below produces an error
print(mystr)
