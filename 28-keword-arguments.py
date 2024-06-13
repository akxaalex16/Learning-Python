def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
# positional arguments; the order matters
greet_user("Akxa", "Beans")
greet_user("Sean", "Beans")

# keyword arguments; the order does not matter
greet_user(last_name="Beans", first_name="Baby")
greet_user(last_name="Beans", first_name="Jovi")
# shows:
# Hi Baby Beans!
# Welcome aboard
# Hi Jovi Beans!
# Welcome aboard
print("Finish")


# example:
def calc_cost(comment, shipping, total, discount):
    print(comment)
    print(total)
    print(shipping)
    print(discount)


calc_cost("Calulating the cost", total=50, shipping=5, discount=0.1)
# prefix the arguments that you pass with the name of their parameters
# keyword arguments should always come after positional arguments
# use keyword arguments when passing numbers so it makes the code easy to read
