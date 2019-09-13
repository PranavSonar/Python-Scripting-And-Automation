# # Print The following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7

# i=7
# for i in range(1,i+1):
#     # print(str(i)+'\n')
#     # print ("i:" +str(i))
#     complete_line=''
#     for k in range(1,i+1):
#         line=str(k)
#         complete_line+=' '+line
#     print (complete_line)


# # Print The following pattern
# 1 1 1 1 1 1 1
# 1 1 1 1 1 2 2
# 1 1 1 1 3 3 3
# 1 1 1 4 4 4 4
# 1 1 5 5 5 5 5
# 1 6 6 6 6 6 6
# 7 7 7 7 7 7 7

# max = 7
# for i in range(1,max+1):
#     complete_line=''
#     for j in range(1,i+1):
#         total_left=max-j

#     for p in range(1,total_left+1):
#         line=' '+str(1)
#         complete_line+=line
#     for q in range(j):
#         line=' '+str(j)
#         complete_line+=line
#     print(complete_line)


# # Print The following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# max =7
# for i in range(1,max+1):
#     complete_line=''
#     for j in range(1,i+1):
#         line=' '+str(j)
#         complete_line+=line
#     print(complete_line)
# for k in range(1,max):
#     complete_line=''
#     for j in range(1,max-k+1):
#         line=' '+str(j)
#         complete_line+=line
#     print(complete_line)


# # Print The following pattern
#  1 2 3 4 5 6 7
#  1 2 3 4 5 6
#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5
#  1 2 3 4 5 6
#  1 2 3 4 5 6 7

# max =20

# for k in range(1,max+1):
#     complete_line=''
#     for j in range(1,max-k+2):
#         line=' '+str(j)
#         complete_line+=line
#     print(complete_line)
# for i in range(2,max+1):
#     complete_line=''
#     for j in range(1,i+1):
#         line=' '+str(j)
#         complete_line+=line
#     print(complete_line)

# # Print The following pattern
# 7 6 5 4 3 2 1
# 7 6 5 4 3
# 7 6 5 4
# 7 6 5
# 7 6
# 7

# max = 7
# for i in range(1, max+1):
#     complete_line = ''
#     for j in range(1, max-i+2):
#         line = ' '+str(max-j+1)
#         complete_line+=line
#     print(complete_line)


# # Print The following pattern
# 7
# 7 6
# 7 6 5
# 7 6 5 4
# 7 6 5 4 3
# 7 6 5 4 3 2
# 7 6 5 4 3 2 1

# max=7
# for i in range(1,max+1):
#     complete_line=''
#     for j in range(1,i+1):
#         line=' '+str(max-j+1)
#         complete_line+=line
#     print(complete_line)


# # Print The following pattern
#  1 2 3 4 5 6 7
#  1 2 3 4 5 6
#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1

# max = 7
# for i in range(0, max):
#     complete_line=''
#     for j in range(1, max-i+1):
#         line=' '+str(j)
#         complete_line += line
#     print(complete_line)


# # Print The following pattern
#  1
#  1 2 1
#  1 2 3 2 1
#  1 2 3 4 3 2 1
#  1 2 3 4 5 4 3 2 1
#  1 2 3 4 5 6 5 4 3 2 1
#  1 2 3 4 5 6 7 6 5 4 3 2 1

# max=7
# for i in range(1,max+1):
#     complete_line=''
#     for j in range(1,i+1):
#         line=' '+str(j)
#         complete_line+=line
#     for k in range(1,i):
#         line=' '+str(i-k)
#         complete_line+=line
#     print(complete_line)


# # Print The following pattern
#  1234567
#   234567
#    34567
#     4567
#      567
#       67
#        7
#       67
#      567
#     4567
#    34567
#   234567
#  1234567


# max = 7
# for i in range(1, max+1):
#     complete_line = ''
#     for j in range(0, max-i+1):
#         line = str(i+j)
#         space = ' '*i
#         complete_line += line
#     complete_line = space+complete_line
#     print(complete_line)
# for k in range(1,max):
#     complete_line=''
#     for p in range(1,max-k+1):
#         space=' '*(p)
#     number=''
#     for q in range(0,k+1):
#         line=str(max-q)
#         number=line+number
#     if len(number) >1 :
#         complete_line+=space+number
#     print(complete_line)


# Print The following pattern
# 1 2 3 4 5 6 7
#  2 3 4 5 6 7
#   3 4 5 6 7
#    4 5 6 7
#     5 6 7
#      6 7
#       7
#      6 7
#     5 6 7
#    4 5 6 7
#   3 4 5 6 7
#  2 3 4 5 6 7
# 1 2 3 4 5 6 7

# max=7
# for i in range(1,max+1):
#     cp_line=''
#     space=' '*i
#     for j in range(0,max-i+1):
#         line=str(max-j)+' '
#         cp_line=line+cp_line
#     cp_line=space+cp_line
#     print(cp_line)
# for k in range(1,max):
#     cp_line=''
#     space=' '*(max-k)
#     for q in range(0,k+1):
#         line=str(max-q)+' '
#         cp_line=line+cp_line
#     cp_line=space+cp_line
#     print(cp_line)


# Print The following pattern
# 1
# 10
# 101
# 1010
# 10101
# 101010
# 1010101

# max=7
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,i+1):
#         if j%2==1:
#             line=str(1)
#         else:
#             line=str(0)
#         cp_line+=line
#     print(cp_line)


# Print The following pattern
# 1010101
# 0101010
# 1010101
# 0101010
# 1010101
# 0101010
# 1010101

# max=7
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(1,max+1):
#         line=str(1)
#         if (i-j)%2==0:
#             line=str(1)
#         else:
#             line=str(0)
#         cp_line+=line
#     print(cp_line)


# Print The following pattern
# 1
# 2 6 
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# i
# i i+max-1
# i i+max-1 (i+max-1)+max-2 (i+max-1)+max-3

# max=5
# for i in range(1,max+1):
#     cp_line=''
#     line=i
#     cp_line+=str(i)+' '
#     for j in range(2,i+1):
#         line=line+max-(j-1)
#         cp_line+=str(line)+' '
#     print(cp_line)





# Print The following pattern
# 0000000
# 0100000
# 0020000
# 0003000
# 0000400
# 0000050
# 0000006


# max=7
# for i in range(max):
#     cp_line=''
#     for j in range(i):
#         line=0
#         cp_line+=str(line)
#     cp_line+=str(i)+str(0)*(max-i)
#     print(cp_line)



