# inheretance to re-use code in other functions or methods instead of copying the code you want to use each time
class Mammal:
    def walk(self):
        print("walk")

# all the methods defined in the Mammal class is now available in the Dog and Cat class
class Dog(Mammal):
    def bark(self):
        print("bark")


class Goat:
    pass


class Cat(Mammal):
    def meow(self):
        print("meow")

dog1 = Dog()
dog1.walk()
# walk() method is inherited
dog1.bark()

cat1 = Cat()
cat1.meow()