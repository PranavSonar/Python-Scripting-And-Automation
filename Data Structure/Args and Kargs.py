# ARGS  TEST
# def myfuc(*args):
#     print(args)
#     # print (args[0])
#     a=[]
#     for i in range(len(args)):
#         print ("Position {} : Number is: {}".format(i,args[i]))
#         a.append(args[i])
#         # a.extend(args)
#         print (a)

# myfuc(1,2,3,23,23,2,3,2,3,24,3322,2,4,34,3,4)

# Take arbitry and return even number only

# def myfunc(*args):
#     a=[]
#     for i in range(len(args)):
#         if args[i] % 2 ==0:
#             a.append(args[i])
#     return a

# print(myfunc(1,2,3,4,5,4,34,3,43,4,34,35,4,54,5,4,5,4,54,5,4))

# to convert all the string or multiple strings
# def myfunc(*args):
#     complete=[]
#     for i in range(len(args)):
#         word = args[i]
#         newWord=''

#         for  j in range(len(word)):
#             if j%2==0:
#                 newWord+=word[j].upper()
#             else:
#                 newWord+=word[j].lower()
#         complete.append(newWord)
#     return complete
# print(myfunc('abc','dssds','dfdfd'))


# to convert a single string
def myfunc(args):
    newWord=''
    for j in range(len(args)):
        if j % 2 == 0:
            newWord += args[j].upper()
        else:
            newWord += args[j].lower()
    return newWord
print(myfunc('abc'))
