# functions are containers for a few lines of code that perform 
# a specific task

# print() and input() are built-in functions

# def to start writing out a function; short for define
# add two lines after every function for best practices
def greeting():
    print("Hi there!")
    print("Welcome aboard")


print("Start")
# the print statements inside the greeting function will only get executed 
# if we call the function; seen below
greeting()
print("Finish")

# you have to call the function after it has been defined, the order matters
# if you call it before the function is defined then there will be an error
# the error shows unresolved refernce

# so the rule is define functions first then we call them