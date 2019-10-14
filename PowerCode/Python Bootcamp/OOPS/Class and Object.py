
class dog():
    # class object attributes
    # same for any isinstance of a class
    species='mammel'
    def __init__(self, breed,name ):
        # Attributes
        # we tahe in the arguments
        # Assign it using self.attribute_name
        self.breed=breed
        self.name=name
    # operations/Actions
    def bark(self,number):
        # pass
        print("Woof!! My Name is {}. My age is {}".format(self.name,number))
    
my_dog=dog(breed='Lab',name='Same')

# my_dog.bark(17)
# print(my_dog.species)

class Circle():
    # class object attribute 
    pi=3.14
    def __init__(self, radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    # Method
    def get_circumference(self):
        return self.radius*self.pi*2

my_circle=Circle(3)
print(my_circle.get_circumference())
print(my_circle.area)