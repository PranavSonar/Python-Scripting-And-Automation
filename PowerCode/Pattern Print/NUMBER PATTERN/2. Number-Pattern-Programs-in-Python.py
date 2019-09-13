# *17 * Printing the pattern... **
# 12345
#  2345
#   345
#    45
#     5
#     5
#    45
#   345
#  2345
# 12345

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(i,max+1):
#         cp_line+=str(j)
#     print(' '*i+cp_line)
# for i in range(2,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         cp_line+=str(max-i+j)
#     print(' '*(max-i+1)+cp_line)

# *18 * Printing the pattern... **
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5
#     5
#    4 5
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5

# max = 5
# for i in range(1, max + 1):
#     cp_line = ''
#     for j in range(i, max + 1):
#         cp_line += str(j) + ' '
#     print(' ' * i + cp_line)
# for j in range(1, max + 1):
#     cp_line = ''
#     for k in range(1, j + 1):
#         cp_line += str(max - j + k) + ' '
#     print(' ' * (max - j+1) + cp_line)

# *19 * Printing the pattern... **
#     5
#    4 5
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         cp_line+=str(max-i+j)+' '
#     print(' '*(max-i)+cp_line)


# *20 * Printing the pattern... **
#     1
#    121
#   12321
#  1234321
# 123454321

# max=10
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         cp_line+=str(j)
#     for k in range(1,i+1):
#         if (i-k)==0:
#             pass
#         else:
#             cp_line+=str(i-k)
#     print(' '*(max-i)+cp_line)


# *21 * Printing the pattern... **
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(i):
#         if j%2==0:
#             cp_line+='1 '
#         else:
#             cp_line+='0 '
#     print(cp_line)


# *22 * Printing the pattern... **
# 1 0 0 0 0
# 0 2 0 0 0
# 0 0 3 0 0
# 0 0 0 4 0
# 0 0 0 0 5

# max=5
# for i in range(max):
#     cp_line=''
#     for j in range(max):
#         if i==j:
#             cp_line+=str(i+1)+' '
#         else:
#             cp_line+='0 '
#     print(cp_line)

# *23 * Printing the pattern... **
# 1 1 1 1 1
# 1 1 1 2 2
# 1 1 3 3 3
# 1 4 4 4 4
# 5 5 5 5 5

# max=5
# for i in range(1,max+1):
#     print('1'*(max-i)+str(i)*i)


# *24 * Printing the pattern... **
# 1 2 3 4 5 4 3 2 1
# 2 3 4 5 4 3 2
# 3 4 5 4 3
# 4 5 4
# 5

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(i,max+1):
#         cp_line+=str(j)+' '
#     for k in range(i+1,max+1):
#         cp_line+=str(max+i-k)+' '
#     print(cp_line)

# *25 * Printing the pattern... **
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5


# max=5
# for i in range(1,max+1):
#   cp_line=''
#   for j in range(i):
#     cp_line+=str(i)+' '
#   cp_line=str(' ')*(max-i)+cp_line
#   print(cp_line)


# *26 * Printing the pattern... **
# 5 5 5 5 5
# 4 5 5 5 5
# 3 4 5 5 5
# 2 3 4 5 5
# 1 2 3 4 5

# max=5
# for i in range(max):
#   cp_line=''
#   for j in range(i):
#       cp_line+=str(max-i+j)
#   cp_line+=str(max)*(max-i)
#   print(cp_line)


# *27 * Printing the pattern... **--------------Unsolved
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# max=5
# for i in range(1,max+1):
#   cp_line=''
#   add=0
#   for j in range(i):
#     cp_line+=str(i+(max-j))+' '

#   print(cp_line)


# *28 * Printing the pattern... **------------Solved
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15
# 6 12
# 7

# max = 4
# for i in range(1,2*max+1):
#         cp_line=''
#         line=i
#         if i <= max:
#                 for j in range(1,i+1):
#                         cp_line+=str(line*j)+' '
#         else:
#                 for k in range(1,max-(i-max)+1):
#                         cp_line+=str(line*k)+' '
#         print (cp_line)

# *29 * Printing the pattern... **-----Unsolved
# 1
# 2 9
# 3 8 10
# 4 7 11 14
# 5 6 12 13 15


# max = 5
# start = 0
# for i in range(1, max+1):
#     cp_line = ''
#     for j in range(i):
#         if j % 2==1:
#             cp_line+=str(start+1)+' '
#             start=j
#         else:
#             cp_line+=str(start-1)+' '
#             start+=(max-j)
#     print(cp_line)


# *30 * Printing the pattern... **
# 1 10 11 20 21
# 2 9  12 19 22
# 3 8  13 18 23
# 4 7  14 17 24
# 5 6  15 16 25


# *31* Printing the pattern... **
# 5 5 5 5 5
# 5 4 4 4 4
# 5 4 3 3 3
# 5 4 3 2 2
# 5 4 3 2 1
max=5

for i in range(1,max+1):
    cp_line=''
    for j in range(max-i):
        cp_line+=str(max-i)
    print(cp_line)

# *32 * Printing the pattern... **[ Fibonacci Triangle Pattern ]
# 1
# 1 2
# 1 2 3
# 1 2 3 5
# 1 2 3 5 8

# max = 5
# prev = 0
# for i in range(1, max+1):
#     cp_line = ''
#     for j in range(i):
#         cp_line += str(j+1)+' '
#     prev = j+1
#     print(cp_line)


# *33 * Printing the pattern... **
# 5
# 4 5 4
# 3 4 5 4 3
# 2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2 1
# 2 3 4 5 4 3 2
# 3 4 5 4 3
# 4 5 4
# 5

# max=5
# for
