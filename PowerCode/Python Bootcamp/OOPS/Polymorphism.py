
# class Dog():
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " Says woof! "


# class Cat():
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " Says Meow!! "


# my_dog = Dog('Motiya')
# print(my_dog.speak())


# my_cat = Cat('Ani')
# print(my_cat.speak())


# for pet_class in [my_cat, my_dog]:
#     print(type(pet_class))
# print(pet_class.speak())


class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclass must implement this abstract method.")


class Dog(Animal):
    def speak(self):
        return self.name+" Says Woof!!"

class Cat(Animal):
    def speak(self):
        return self.name+" Says meow!!"

my_dog = Dog("Motiya")
my_cat = Cat("Catiya")
print(my_dog.speak())
print(my_cat.speak())
