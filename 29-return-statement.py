# use the return statement so we can use the result 
# of that function outside of the function, when we store it in a variable
def square(number):
    return number * number


result = square(3)
print(result)

# you can also just write:
print(square(3))

# have a return statement or print statement at the end of the function
# by default all functions in python return None, unless there is a return statement to show a result
