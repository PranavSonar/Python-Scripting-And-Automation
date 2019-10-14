import One

print("TOp level in two.py")
One.func()
if __name__=='__main__':
    print("Two.py is being run directly!!")
else:
    print("Two.py Imported!!")