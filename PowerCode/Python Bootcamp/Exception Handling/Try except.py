try:
    f = open('testfile', "r")
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error!")
except:
    print("Except all other error.")
finally:
    print("Hey Hello that's me with full permission to exec all time.")




