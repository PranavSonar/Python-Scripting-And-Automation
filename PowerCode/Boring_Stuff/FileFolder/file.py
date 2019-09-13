# import os
# path = os.path.join('abcv', 'dsd')

# print(path)

# b = os.getcwd()
# print("Hello")
# print(b)
# os.chdir(b)
# c = os.path.abspath(b)
# print(c)

# d = c+'FileFolder//file.py'

# print(os.path.getsize(c))
# print(os.listdir(c))

# c = 'D:'
# total_size = 0
# for filename in os.listdir(c):
#     # if not os.path.isfile(os.path.join(c,filename)):
#     #     continue
#     total_size = total_size+os.path.getsize(os.path.join(c, filename))
#     print(filename, str(total_size))

# # for i in range(100):
# #     c = c+'//This is folder'+str(i)
# #     print (c)
# #     # print(os.makedirs(c))


test_file=open('D:/Programs/WorkArea/Code-Challenge/Python/Boring_Stuff/FileFolder/file.py')
file_conten=test_file.read()

# print(file_conten)

test_file.close()

test_file=open('D:/Programs/WorkArea/Codef-Challenge/Python/Boring_Stuff/FileFolder/file.py')

print(test_file.readlines()[2])

