# how to handle errors in python programs
# try and except
# in the try block we write what we want to happen
# in the except block we write what to do if there is an error, so it wont crash if the user puts something invalid
# the exit code will be 0, even if it falls into the exception

try:
    age = int(input("Age: "))
    income = 80000
    risk = income / age
    # if we run this and input 0, then we get ZeroDivisionError: division by zero
    # because we cannot divide a number by zero
    print(age)
except ZeroDivisionError:
    print('Age can not be 0')
except ValueError:
    print('Invalid value')

# if we put in a number as the input we get:
# process finished with exit code 0
# but if we put random letters like 'ash', then we get:
# ValueError: invalid literal for int() with base 10: 'ash'
# and it shows process finished with exit code 1 
# any exit code besides 0, means that it crashed