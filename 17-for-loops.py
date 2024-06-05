# used to iterate over items of a collection, such as strings or lists

# iterating over a string
for item in "Python":
    print(item) 
# the results show:
# P
# y
# t
# h
# o
# n

# iterating over a list of strings
for item in ["Akxa", "Sean", "Bean", "Baby Luv", "Jovi", "Alex", "Hupe"]:
    print(item)

# iterating over a list of numbers
for item in [3,6,9,16]:
    print(item)

# iterating over a large list of numbers or an object
# use the range function
for item in range(10):
    print(item)
# shows numbers 0-9

# another example
for item in range(5,10):
    print(item)
# shows 5-9

# range function can additionally take in a step
# third vaue is the step, shows how much to go up by
for item in range(5,10,2):
    print(item)
# shows:
# 5
# 7
# 9

# challenge:
# get the total cost of all the items in a shopping cart

prices = [16, 6, 9, 3]

total = 0

for price in prices:
    total += price
print(f"Total: ${total}")