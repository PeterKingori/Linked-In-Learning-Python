#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#

# define a basic function
def function1():
    print("I'm a function")

# function that takes arguments
def function2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return  x * x * x

# function with default value for an argument
def power(num, valuex = 1):
    result = 1
    for i in range(valuex):
        result = result * num
    return result

# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


function1()
print(function1())
print(function1)

function2(20, 234634)
print(function2(20, 234634))
function2("Hello", "New York!")
print(cube(4))

print(power(2))
print(power(2, 3))

print(multi_add(4, 9, 12, 987))
