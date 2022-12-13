# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

def is_palindrome(input_string):
    # use the slice trick to reverse the string
    if input_string == input_string[::-1]:
        return True
    return False

RUN = True
while RUN:
    user_input = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit" then quit the program
    if user_input == "exit":
        RUN = False
        break

    # convert the string to all lower case
    user_input = user_input.lower()

    # strip all the spaces and punctuation from the string
    new_string = ""
    for x in user_input:
        if x.isalnum():
            new_string += x

    print("Palindrome test:", is_palindrome(new_string))
