class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # initializing code
        # self is a reference to the current object
        # self references point = Point(10, 20), that objet in memory 

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
# we get an AttributeError: 'Point' object has no attribute 'x'
# to solve this problem, we use a constructor
# a constructor is a function that gets called at the time of creating an object
# if we add any values on line 16, like point = Point(10, 20), now the point object will have its x and y coordinates initialized 
# so we create a special method in the class Point called a constuctor
# def __init__(self) 
# this is the function or method that gets called when we create a new point object

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi I am {self.name}")

person = Person("Akxa")
print(person.name)
person.talk()

person2 =Person("Sean")
person2.talk()