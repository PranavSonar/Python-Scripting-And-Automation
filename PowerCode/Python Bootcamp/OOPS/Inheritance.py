# Program to show example of inheritence in python
class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("Ooo, Hi am an Animal. Its an not a...:)")

    def eat(self):
        print("I can eat as well you know...")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created..")
        self.name="Oops"

    def who_am_i(self):
        print("Thats me your Dog One:)")
    def bark(self):
        print("Woof !! {}".format(self.name))


my_animal = Dog()
my_animal.who_am_i()
my_animal.bark()
my_animal.eat()