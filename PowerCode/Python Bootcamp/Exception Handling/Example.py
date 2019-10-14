
# try:
#     for i in range['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print("I Type Error!!")


# try:
#     x = 5
#     y = 0
#     z = x/y
# except ZeroDivisionError:
#     print("Look Like you are trying to devide by Zero!!!")


def ask():
    # waiting for correct response
    waiting=True
    while waiting:
        try:
            n = int(input("Enter a number"))
        except:
            print("Please Try Again ! \n")
            continue
        else:
            waiting=False
    print("Your Number squared is: ")
    print(n**2)
ask()