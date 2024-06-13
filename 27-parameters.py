# how to pass information to your function

# inside the parentheses of our function we can have parameters,
# which are placeholders for recieving information

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("Akxa", "Beans")
greet_user("Sean", "Beans")
print("Finish")

# argument is the value that we supply to a function

# when a function has a parameter, then we are obligated to pass a value for that parameter
# so if we dont provide an argument when the function is called, and that function
# being called has a parameter, then it will give TypeError: greet_user() missing 
# one required positional argument


