# Magic methord
# 1. __init__() #--automatically called when object is created
# 2. __str__() #--it will return string represention of object
# 3. __len__() #--it will return length which we can set in program
# 4. __del__() #--it will delete the variable when delete the object


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "{} by {}, Total pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object is deleted")


b1 = Book('python book', 'Jose', 100)

print(b1)
print(str(b1))
print(len(b1))
# del(b1)
# del b1

print(dir(b1))