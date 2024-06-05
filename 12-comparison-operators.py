# condition:
# if temperature is greater than 30
#     it is a hot day 
# otherwise if it is less than 10
#     it is a cold day
# otherwise 
#     it is neither hot nor cold

# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to
# == equal
# != not equal

temperature = 16

if temperature > 30:
    print("It is a hot day")
elif temperature < 10:
    print("It is a cold day")
else:
    print("It is neither hot or cold")

# another example:
# if name is less than 3 characters long
#   name must be at least 3 characters long
# otherwise if it is more than 50 characters long
#   name can be a maximum of 50 characters
# otherwise 
#   name looks good

name="Akxa Bean Alex"

if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 50:
    print('Name can be a max of 50 characters')
else:
    print("Name looks good")