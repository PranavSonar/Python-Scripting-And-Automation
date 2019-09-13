#32 # Printing the pattern ##
# *    *
#  *  *
#   *
#  *  *
# *    *

# max=10
# for i in range(int(max/2)):
#     print(' '*i+'*'+' '*(2*max-2*i-max-1)+'*')
# if max%2 ==1:
#     print(' '*int((max-1)/2)+'*')
# else:
#     print(' '*int((max-1)/2+1)+'*')
# for i in range(int(max/2)):
#     print(' '*(int(max/2)-i-1)+'*'+' '*(2*i+1)+'*')


#33 # Printing the pattern ##
#     *
#     *
#     *
#     *
# *********
#     *
#     *
#     *
#     *
# max=5
# for i in range(max-1):
#     print(' '*(max-1)+'*')
# print('*'*(2*max-1))
# for i in range(max-1):
#     print(' '*(max-1)+'*')


#34 # Printing the pattern ##
#  ***
# *   *
# *   *
# *   *
#  ***
# *   *
# *   *
# *   *
#  ***
max=5
print(' '+'*'*(max-2))
for i in range(max-2):
    print('*'+' '*(max-2)+'*')
print(' '+'*'*(max-2))
for i in range(max-2):
    print('*'+' '*(max-2)+'*')
print(' '+'*'*(max-2))