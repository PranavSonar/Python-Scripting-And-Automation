#one.py

def func():
    print("Function Func() in one.py")

print("Top Level Indentation!!!")

if __name__=='__main__':
    print("One.py is running directly")
    print(__name__)
else:
    print("one.py has been imported")
    print(__name__)