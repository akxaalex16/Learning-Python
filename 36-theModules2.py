import theModules
# importing all methods, then follow to line 11 to access it

from theModules import lbs_to_kg
# you can import specific methods also, you dont have to import the whole file
# and use it directly in this file
# dont need to prefix it with the module or file name
print(lbs_to_kg(105))

# we can use the dot operator to accesss the methods fromm the other file
print(theModules.kg_to_lbs(45))


# from challenge
from theModules import find_max

numbers = [3, 6, 10, 16, 10]
# max = find_max(numbers)
print(max(numbers))