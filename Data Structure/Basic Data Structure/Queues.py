# This is a queues practices sheet
# queue : FIFO: First In first Out
# using collecion deque dual ended queues

# from collections import deque
# my_queue=deque()
# my_queue.append(5)
# my_queue.append(10)
# my_queue.append(10)
# my_queue.popleft()
# print(my_queue)

# using list implemation


from collections import deque


class queue():
    # to create new queue using list
    def __init__(self):
        self.queue = list()
    # to enter new element

    def enqueue(self, item):
        self.queue.append(item)
        print(self.queue)

    # to remove front element1

    def dequeue(self):
        self.queue.pop(0)
    # to get front element of queue

    def front(self):
        if len(self.queue) > 0:
            return(self.queue[0])

        else:
            return None
    # to get rear element of queue

    def rear(self):
        if len(self.queue) > 0:
            return(self.queue[len(self.queue)-1])
        else:
            return None
    # to get size of queue

    def get_size(self):
        return len(self.queue)
    # to get complete queue

    def __str__(self):
        return str(self.queue)

    def clear_queue(self):
        return self.queue.clear()


# init object
my_queue = queue()
while True:
    print('''\n\nLets Play with Queue : 
            1. Insert(Enqueue) Items
            2. Remove(Dequeue) Items
            3. Front Item View
            4. Rear Item View
            5. Size of Queue
            6. View Complete Queue
            7. Remove(Clear) All Items
        \nCurrent Queue: {}
            '''.format(my_queue.__str__()))
    choice = int(input("Enter Choice:"))
    if choice == 1:
        item = input("Enter Items :")
        my_queue.enqueue(item)
    elif choice == 2:
        my_queue.dequeue()
    elif choice == 3:
        print(my_queue.front())
    elif choice == 4:
        print(my_queue.rear())
    elif choice == 5:
        print(my_queue.get_size())
    elif choice == 6:
        print(my_queue.__str__())
    elif choice == 7:
        my_queue.clear_queue()
    else:
        print("Invalid option: "+str(choice))


# Works
class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def get_size(self):
        return len(self.queue)-1
