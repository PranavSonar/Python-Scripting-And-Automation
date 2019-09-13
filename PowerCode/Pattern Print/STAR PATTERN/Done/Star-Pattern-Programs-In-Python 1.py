# All the Test Pattern Taken from https://www.javainterviewpoint.com/star-pattern-programs-in-java/

# 1 # Print The following pattern
# *
# **
# ***
# ****
# *****

# limit=50
# for i in range(1,limit+1):
#     for j in range(i,i+1):
#         print(str('*')*j)

# 2 # Print The following pattern
#     *
#    **
#   ***
#  ****
# *****

limit=5
for i in range(1,limit+1):
        print(str(' ')*(limit-i)+'*'*i)

# 3 # Print The following pattern
# *****
# ****
# ***
# **
# *
# limit=5
# for i in range(limit):
#     print(str('*')*(limit-i))


# 4# Printing the pattern ##
# *****
#  ****
#   ***
#    **
#     *
# limit=5
# for i in range(limit):
#     print(str(' ')*i+str('*')*(limit-i))


#5 # Printing the pattern ##
#     *
#    ***
#   *****
#  *******
# *********

# limit=20
# for i in range(1,limit+1):
#     print(str(' ')*int(limit-i)+'*'*i+'*'*(i-1))

#6 # Printing the pattern ##
# *********
#  *******
#   *****
#    ***
#     *

# limit=5
# for i in range(limit):
#     print(str(' ')*i+'*'*(limit-i)+'*'*(limit-i-1))


#7 # Printing the pattern ##
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# limit=5
# for i in range(1, limit+1):
#     print(str(' ')*(limit-i)+str('*')*(i-1)+'*'*(i))
# for i in range(1,limit):
#     print(str(' ')*i+str('*')*(limit-i)+'*'*(limit-i-1))


#8 # Printing the pattern ##
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# limit=5
# for i in range(1,limit+1):
#     print(str('*')*i)
# for i in range(1,limit):
#     print(str('*')*(limit-i))

#9 # Printing the pattern ##
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# limit=5
# for i in range(1,limit+1):
#     print(str(' ')*(limit-i)+str('*')*i)
# for i in range(1,limit):
#     print(str(' ')*i+str('*')*(limit-i))

#10 # Printing the pattern ##
#     *****
#    *****
#   *****
#  *****
# *****

# limit=5
# for i in range(limit):
#     print(str(' ')*(limit-i)+str('*')*limit)

#11 # Printing the pattern ##
# *****
#  *****
#   *****
#    *****
#     *****

# limit=5
# for i in range(limit):
#     print(str(' ')*(i)+str('*')*limit)


#12 # Printing the pattern ##
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****
# limit=5
# for i in range(limit):
#     print(str('*')*(limit-i))
# for i in range(2,limit+1):
#     print(str('*')*(i))


#13 # Printing the pattern ##
# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****

# limit=5
# for i in range(1,limit+1):
#     cp_line=''
#     space=''
#     for j in range(limit-i+1):
#         cp_line=cp_line+'*'
#     for k in range(i):
#         space+=' '
#     print(space+cp_line)
# for p in range(2,limit+1):
#     space_1=''
#     cp_line_1=''
#     for q in range(p):
#         cp_line_1=cp_line_1+'*'
#     for r in range(limit-p+1):
#         space_1+=' '
#     print(space_1+cp_line_1)

# limit=5
# for i in range(1,limit+1):
#     print(' '*i+'*'*(limit-i+1))
# for i in range(2,limit+1):
#     print(' '*(limit-i+1)+'*'*i)

#14 # Printing the pattern ##
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# limit=5
# for i in range(1,limit+1):
#     print(' '*i+'* '*(limit-i+1))
# for i in range(2,limit+1):
#     print(' '*(limit-i+1)+'* '*i)

#15 # Printing the pattern ##
# *
# **
# * *
# *  *
# *****

# max=7
# print('*')
# for i in range(1,max-1):
#     print('*'+' '*(i-1)+'*')
# print('*'*max)

#16 # Printing the pattern ##
#     *
#    **
#   * *
#  *  *
# *****
# max=5
# print(' '*(max-1) +'*')
# for i in range(1,max-1):
#     print(' '*(max-i-1)+'*'+' '*(i-1)+'*')
# print('*'*max)


