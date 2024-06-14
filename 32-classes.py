# basic types:
# numbers
# strings
# booleans

# complex types:
# lists
# dictionaries

# we use classes to define new types
# point
# it has methods like: move, draw, get_distance from another point

# we start by defining a class by using the class keyword
# followed by the name of the class, capitalize the first letter of every word when naming classes (pascal naming convention)
class Point:
    # in this block we can define all the functions or methods that belong to points
    def move(self): 
        print('move')

    def draw(self):
        print('draw')


# so with this class we difined a new type, with this 
# new type we can create new objects
# an object is an instance of a class

# a class simply defines the blueprint or the template for creating objects,
# and objects are the actual instances based on that blueprint

# to create an object and return it, we call the class like a function
# then we can store that object in a variable
point1 = Point()

# now when we use the dot operator, we can see the two methods that we defined in the class
point1.draw()
# prints draw on the terminal
point1.move()
# prints move on the terminal

# attributes 
point1.x = 10
point1.y = 20
print(point1.x)

# create another object
point2 = Point()
point2.x= 16
print(point2.x)