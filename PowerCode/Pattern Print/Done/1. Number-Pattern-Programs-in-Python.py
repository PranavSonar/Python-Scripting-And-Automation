# # # All the Test Pattern Taken from https://www.javainterviewpoint.com/number-pattern-programs-in-java/

# *1 * Printing the pattern... **
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for i in range(1,i+1):
#         line=str(i)+' '
#         cp_line+=line
#     print(cp_line)

# *2 * Printing the pattern... **
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         line=str(i)+' '
#         cp_line+=line
#     print(cp_line)

# *3 * Printing the pattern... **
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(i):
#         cp_line+=str(j+1)+' '
#     print(cp_line)
# for i in range(1,max):
#     cp_line=''
#     for j in range(max-i):
#         cp_line+=str(j+1)+' '
#     print(cp_line)

# *4 * Printing the pattern... **
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# max=20
# for i in range(max):
#     cp_line=''
#     for j in range(1,max-i+1):
#         cp_line+=str(j)+' '
#     print(cp_line)
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         cp_line+=str(j)+' '
#     print(cp_line)

# *5 * Printing the pattern... **
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# max=5
# for i in range(max):
#     cp_line=''
#     for j in range(max-i):
#         cp_line+=str(max-i-j)+' '
#     print(cp_line)
# for i in range(max):
#     cp_line=''
#     for j in range(i+1):
#         cp_line+=str(i-j+1)+' '
#     print(cp_line)

# *6 * Printing the pattern... **
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

# max = 5
# for i in range(1, max+1):
#     cp_line = ''
#     for j in range(1, i+1):
#         cp_line += str(j)+' '
#     cp_line = ' '*(max-i) + cp_line
#     print(cp_line)

# *7 * Printing the pattern... **
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# max=5
# for i in range(max):
#     cp_line=''
#     for i in range(max-i):
#         cp_line+=str(max-i)+' '
#     print(cp_line)

# *8 * Printing the pattern... **
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# max=5
# for i in range(max):
#     cp_line=''
#     for j in range(i+1):
#         cp_line+=str(max-j)+' '
#     print(cp_line)

# *9 * Printing the pattern... **
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# max=50
# for i in range(max):
#     cp_line=''
#     for j in range(1,max-i+1):
#         cp_line+=str(j)+' '
#     print(cp_line)

# *10 * Printing the pattern... **
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# max = 5
# add=0
# for i in range(1, max+1):
#     cp_line = ''
#     for j in range(add,i+add):
#         line = i+j
#         cp_line += str(line)+' '
#         add=j
#     print(cp_line)

# *11 * Printing the pattern... **
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         cp_line+=str(i-j+1)+' '
#     print(cp_line)

# *12 * Printing the pattern... **
# 1
# 2 7
# 3 8 13
# 4 9 14 19
# 5 10 15 20 25

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(i):
#         cp_line+=str(i+j*max)+' '
#     print(cp_line)

# *13 * Printing the pattern... **
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Assignment Programs-Pascal Triangle Shorter Code
# max = 5
# def factrial_of_number(n):
#         if n==1 or n==0:
#                 return 1
#         else:
#                 return n*factrial_of_number(n-1)
# # print (factrial_of_number(4))
# for i in range(max):
#     cp_line = ''
#     for j in range(i+1):
#         # nCr=n!/r!*(n-r)!
#         line=int(factrial_of_number(i)/(factrial_of_number(j)*factrial_of_number(i-j)))
#         cp_line += str(line)+' '
#     cp_line = ' ' * (max - i) + cp_line
#     print(cp_line)

# *14 * Printing the pattern... **
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

# max=5
# for i in range(1,max+1):
#         cp_line=''
#         for j in range(1,i+1):
#                 line=str(j)
#                 cp_line+=line+' '
#         for k in range(1,i):
#                 line=str(i-k)
#                 cp_line+=line+' '
#         print(cp_line)


# *15 * Printing the pattern... **
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

# max=5
# for i in range(max):
#         cp_line=''
#         for j in range(1,max-i+1):
#                 line=str(j)+' '
#                 cp_line+=line
#         cp_line=' '*i+cp_line
#         print(cp_line)

# *16 * Printing the pattern... **
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

# max=10
# for i in range(1,max+1):
#         cp_line=''
#         for j in range(1,i+1):
#                 cp_line+=str(j)+' '
#         print(' '*(max-i)+cp_line)
# for k in range(1,max):
#         cp_line=''
#         for p in range(1,max-k+1):
#                 cp_line+=str(p)+' '
#         print(' '*k+cp_line)