# built-in modules in Python
# like sending emails, working with date and time, generating random values and passwords, etc.
# search for python 3 module index to get a list of built-in modules
# import the random module

import random

# access random method
# generates random value from 0-1
random.random()

# generate 3 random numbers 
for i in range(3):
    print(random.random())

# to generate random values between 10 and 20
for i in range(3):
    print(random.randint(10, 20))

# randomly pick a leader from a list of members
members = ["Akxa", "Sean", "Baby Luv", "Jovi"]
leader = random.choice(members)
print(leader)


# challenge roll a dice and get 2 values

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
        

selection = Dice()
print(selection.roll())
