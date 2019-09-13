# print("This Is a Stack Practic Sheet")
# # Creating stack

# # Implementing the stack using list


class stack():
    # creating a empty stack
    def __init__(self):
        self.stack = list()
    # pushing into stack

    def push(self, item):
        self.stack.append(item)
    # pop from stack

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    # peek/top of item of stack

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return 123
    # to define {Devison}e function can be called with multiple name
    top = peek
    # getting the stack string

    def __str__(self):
        return str(self.stack)


a1 = stack()
while True:
    print('''\nNow Stack is Implemented so you can do following operation on it.
                1. Insert(PUSH) item
                2. Remove Last(POP) items
                3. View All Items
                4. View Top Items
            ''')
    choice=input("Enter you choice :")
    if choice =='1':
        print('1. Insert(PUSH) item')
        item=input("Enter Items :")
        a1.push(item)
    elif choice=='2':
        print("2. Remove Last(POP) items")
        print(a1.pop())
    elif choice=='3':
        print ("3. View All Items")
        print(a1.__str__())
    elif choice=='4':
        print("4. View Top Items")
        print(a1.peek())
    else:
        print("Invalid option: "+str(choice))