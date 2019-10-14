def ask_for_int():
    while True:
        try:
            result=int(input("Please provide number:"))
        except:
            print("Whoops! Thats is not a number")
            continue
        else:
            print(" Int Yes Thanks You")
            break
        finally:
            print("End of try/except/Finally Block")
            print("I Will always Run at the end")
    

ask_for_int()