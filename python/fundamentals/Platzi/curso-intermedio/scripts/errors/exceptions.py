def palindrome(string):
    try:
        if string == 0:
            raise ValueError("The string is empty")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
        

"""
# A traceback will appears showing a Type error
palindrome(1)
"""

"""
# Code to handle the exception
try:
    palindrome(1)
except TypeError:
    print("Error: Strings are the only type of input allowed")
"""