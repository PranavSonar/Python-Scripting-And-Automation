# It is use to add new funcinility to an existing function without change older function
# syntax :
# @some_decortor
# def some_func():
#     return something



# def cool():
#     def super_cool():
#         return 'I am very cool!'
#     return super_cool

# some_func=cool()
# print(some_func())


# def hello():
#     return 'Hi Jose!'

# def other(some_func):
#     print("Do some silly thing")
#     print(some_func())

# other(hello)




def new_decorator(original_func):
    def wrap_fun():
        print("soome extre code of deco")
        original_func()
        print("Aftre func code")
    return wrap_fun

@new_decorator
def func_needs_decprator():
    print("I want to be decorated!!")

# decorated_func=new_decorator(func_needs_decprator)

# decorated_func()

func_needs_decprator()

