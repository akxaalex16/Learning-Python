# how to get input from user
#you always get a string as the value
name=input("What is your name?  ")
msg=f'hi {name}'
print(msg) 
# or print('Hi' + name)


# example: ask 2 questions: person's name and fav color
# then print a message like "Bean likes black"
name1=input("What is your name? ")
fav_color=input("What is your favorite color? ")
print(name1 + " likes " + fav_color)


# example: ask a user their weight in pounds,
# convert it to kilograms and print on the terminal

weight_lbs=input("What is your weight in lbs? ")
weight_kg= int(weight_lbs)//2.2
print(weight_kg)