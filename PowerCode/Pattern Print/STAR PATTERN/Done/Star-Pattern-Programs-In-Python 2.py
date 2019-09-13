#17 # Printing the pattern ##
# *****
# *  *
# * *
# **
# *

# max=5
# print('*'*(max))
# for i in range(1,max-1):
#     print('*'+' '*(max-i-2)+'*')
# print('*')

#18 # Printing the pattern ##
# *****
#  *  *
#   * *
#    **
#     *

# max=5
# print('*'*max)
# for i in range(1,max-1):
#     print(' '*(i)+'*'+' '*(max-i-2)+'*')
# print(' '*(max-1)+'*')

#19 # Printing the pattern ##
#     *
#    * *
#   *   *
#  *     *
# *********

# max=5
# print(' '*(max-1)+'*')
# for i in range(1,max-1):
#     print(' '*(max-i-1)+'*'+' '*(2*i-1)+'*')
# print('*'*(2*max-1))

#20 # Printing the pattern ##
# *********
#  *     *
#   *   *
#    * *
#     *

# max = 5
# print('*'*(2*max-1))
# for i in range(1,max-1):
#     print(' '*(i)+'*'+' '*(2*max-2*i-3)+'*')
# print(' '*(max-1)+'*')


#21 # Printing the pattern ##
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

# max=5
# print(' '*(max-1)+'*')
# for i in range(1,max):
#     print(' '*(max-i-1)+'*'+' '*(2*i-1)+'*')
# for i in range(1,max-1):
#     print(' '*i+'*'+' '*(2*max-2*i-3)+'*')
# print(' '*(max-1)+'*')


#22 # Printing the pattern ##
# *
# **
# * *
# *  *
# *   *
# *  *
# * *
# **
# *


# max=50
# print('*')
# for i in range(0,max-1):
#     print('*'+' '*i+'*')
# for j in range(1,max-1):
#     print('*'+' '*(max-j-2)+'*')
# print('*')

#23 # Printing the pattern ##
#     *
#    **
#   * *
#  *  *
# *   *
#  *  *
#   * *
#    **
#     *


# max=5
# print(' '*(max-1)+'*')
# for i in range(1,max):
#     print(' '*(max-i-1)+'*'+' '*(i-1)+'*')
# for i in range(1,max-1):
#     print(' '*(i)+'*'+' '*(max-i-2)+'*')
# print(' '*(max-1)+'*')


#24 # Printing the pattern ##
#     *****
#    *   *
#   *   *
#  *   *
# *****

# max=5
# print(' '*(max-1)+'*'*max)
# for i in range(2,max):
#     print(' '*(max-i)+'*'+' '*(max-2)+'*')
# print('*'*max)

#25 # Printing the pattern ##
# *****
#  *   *
#   *   *
#    *   *
#     *****

# max=10
# print('*'*max)
# for i in range(1,max-1):
#     print(' '*i+'*'+' '*(max-2)+'*')
# print(' '*(max-1)+'*'*max)

#26 # Printing the pattern ##
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# max=5
# for i in range(1,max+1):
#     print('*'*i+' '*(2*max-2*i)+'*'*i)
# for i in range(1,max+1):
#     print('*'*(max-i)+' '*(2*i)+'*'*(max-i))



#27 # Printing the pattern ##
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# max=5
# for i in range(max):
#     print('*'*(max-i)+' '*2*i+'*'*(max-i))
# for i in range(1,max+1):
#     print('*'*i+' '*(2*max-2*i)+'*'*i)


#28 # Printing the pattern ##
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

# max=5
# print(' '*(max)+'*')
# for i in range(1,max):
#     print(' '*(max-i)+'*'+' '*(2*i-1)+'*')
# for i in range(2,max):
#     print(' '*i+'*'+' '*(2*max-2*i-1)+'*')
# print(' '*(max)+'*')

#29 # Printing the pattern ##
# * * * * *
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# * * * * *

# max=5
# print(max*'* ')
# for i in range(1,max-1):
#     print(' '*i+'*'+' '*(2*max-2*i-3)+'*')
# print(' '*(max-1)+'*')
# for i in range(2,max):
#     print(' '*(max-i)+'*'+' '*(2*i-3)+'*')
# print(max*'* ')

#30 # Printing the pattern ##
# *****
# *****
# *****
# *****
# *****

# max=5
# for i in range(max):
#     print('*'*max)


#31 # Printing the pattern ##
# *****
# *   *
# *   *
# *   *
# *****

# max=5
# print('*'*max)
# for i in range(max-2):
#     print('*'+' '*(max-2)+'*')
# print('*'*max)
