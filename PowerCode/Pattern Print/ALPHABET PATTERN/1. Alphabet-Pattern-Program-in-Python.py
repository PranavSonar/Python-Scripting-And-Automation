# # All the Test Pattern Taken from https://www.javainterviewpoint.com/alphabet-pattern-program/


# # *1 * Printing the pattern... **
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F

# max=5
# Start_CAPs_Alphabets=65
# for i in range(1,max+2):
#     cp_line=''
#     for j in range(i):
#         cp_line+=chr(Start_CAPs_Alphabets+j)+' '
#     print cp_line

# *2 * Printing the pattern... **
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# F F F F F F


# max=5
# for i in range(1,max+2):
#     cp_line=''
#     for j in range(1,i+1):
#         cp_line+=chr(65+i-1)+' '
#     print cp_line


# *3 * Printing the pattern... **
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A


# max=5
# for i in range(1,max+2):
#     cp_line=''
#     for j in range(i):
#         cp_line+=chr(65+j)+' '
#     print cp_line
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(max-i+1):
#         cp_line+=chr(65+j)+' '
#     print cp_line


# *4 * Printing the pattern... **
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F

# max=5
# for i in range(0,max+1):
#     cp_line=''
#     for j in range(0,max-i+1):
#         cp_line+=chr(65+j)+' '
#     print cp_line
# for i in range(0,max+1):
#     cp_line=''
#     for j in range(i+1):
#         cp_line+=chr(65+j)+' '
#     print cp_line

# *5 * Printing the pattern... **
# F E D C B A 
# E D C B A 
# D C B A 
# C B A 
# B A 
# A 
# A 
# B A 
# C B A 
# D C B A 
# E D C B A 
# F E D C B A

# max=6
# for i in range(max):
#     cp_line=''
#     for j in range(1,max-i+1):
#         cp_line+=chr(65+max-j-i)+' '
#     print (cp_line)
# for p in range(1,max+1):
#     cp_line=''
#     for q in range(p):
#         cp_line+=chr(64-q+p)+' '
#     print(cp_line)

# *6 * Printing the pattern... **
#      A 
#     A B 
#    A B C 
#   A B C D 
#  A B C D E 
# A B C D E F

# max=6
# for i in range(1,max+1):
#     cp_line=''  
#     for j in range(i):
#         cp_line+=chr(65+j)+' '
#     cp_line=' '*(max-i)+cp_line
#     print(cp_line)

# *7 * Printing the pattern... **
# F E D C B A 
# F E D C B 
# F E D C 
# F E D 
# F E 
# F 

# max=6
# for i in range(max):
#     cp_line=''
#     for j in range(max-i):
#         cp_line+=chr(64+max-j)+' '
#     print(cp_line)



# *8 * Printing the pattern... **
# F 
# F E 
# F E D 
# F E D C 
# F E D C B 
# F E D C B A

# max=6
# for i in range(max):
#     cp_line=''
#     for j in range(i+1):
#         cp_line+=chr(64+max-j)+' '
#     print(cp_line)
        
         

# *9 * Printing the pattern... **
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 


# max=6
# for i in range(max):
#     cp_line=''
#     for j in range(max-i):
#         cp_line+=chr(64+j+1)+' '
#     print(cp_line)
    

# *10 * Printing the pattern... **
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# P Q R S T U

# max=6
# add=0
# for i in range(1,max+1):
#     cp_line=''
#     for j in range(add,i+add):
#         cp_line+=chr(64+i+j)+' '
#         add=j
#     print(cp_line)






# *11 * Printing the pattern... **
# A 
# B A 
# C B A 
# D C B A 
# E D C B A 
# F E D C B A

# max=6
# for i in range(max):
#   cp_line=''
#   for j in range(i+1):
#     cp_line+=chr(65+i-j)+' '
    
#   print(cp_line)

# *12 * Printing the pattern... **
# A 
# B G 
# C H M 
# D I N S 
# E J O T Y 
# F K P U Z _
# ----------------------------------------------------------->

  
# *13 * Printing the pattern... **
#      A 
#     A A 
#    A B A 
#   A C C A 
#  A D F D A 
# A E J J E A

max=6
for i in range(1,max+1):
  cp=''
  for j in range(1,i+1):
    cp+=chr(64+i+j)+' '
  cp=' '*(max-i)+cp
  print(cp)

# *14 * Printing the pattern... **
# A 
# A B A 
# A B C B A 
# A B C D C B A 
# A B C D E D C B A 
# A B C D E F E D C B 

# *15 * Printing the pattern... **
#  A B C D E F 
#   A B C D E 
#    A B C D 
#     A B C 
#      A B 
#       A

# *16 * Printing the pattern... **
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E 
#  A B C D E F 
#   A B C D E 
#    A B C D 
#     A B C 
#      A B 
#       A

# *17 * Printing the pattern... **
# ABCDEF
#  BCDEF
#   CDEF
#    DEF
#     EF
#      F
#      F
#     EF
#    DEF
#   CDEF
#  BCDEF
# ABCDEF

# *18 * Printing the pattern... **
# A B C D E F 
#  B C D E F 
#   C D E F 
#    D E F 
#     E F 
#      F 
#      F 
#     E F 
#    D E F 
#   C D E F 
#  B C D E F 
# A B C D E F

# *19 * Printing the pattern... **
#      F 
#     E F 
#    D E F 
#   C D E F 
#  B C D E F 
# A B C D E F

# *20 * Printing the pattern... **
#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA
# ABCDEFEDCBA

# *21 * Printing the pattern... **
# A A A A A A 
# A A A A B B 
# A A A C C C 
# A A D D D D 
# A E E E E E 
# F F F F F F

# *22 * Printing the pattern... **
# A B C D E F E D C B A 
# B C D E F E D C B 
# C D E F E D C 
# D E F E D 
# E F E 
# F 

# *23 * Printing the pattern... **
#      A 
#     B B 
#    C C C 
#   D D D D 
#  E E E E E 
# F F F F F F 

# *24 * Printing the pattern... **
# Enter the String which needs to be printed 
# JAVA
# ** Printing the pattern... **
#    J
#   AAA
#  VVVVV
# AAAAAAA


# *25 * Printing the pattern... **
# A 
# C B 
# D E F 
# J I H G 
# K L M N O

# *26 * Printing the pattern... **
# A 
# B C 
# F E D 
# G H I J 
# O N M L K

# *27 * Printing the pattern... **
# ABCDE
# BCDEF
# CDEFG
# DEFGH
# EFGHI

# *28 * Printing the pattern... **
# ABCDEDCBA
# ABCDCBA
# ABCBA
# ABA
# A