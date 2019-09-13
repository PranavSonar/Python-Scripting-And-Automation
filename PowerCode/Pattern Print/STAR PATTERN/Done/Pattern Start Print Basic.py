#%%
# code to print box/O
# *****
# *   *
# *   *
# *   *
# *   *
# *   *
# *****

def boxPrint(symbol, width, hight):
    print(symbol*width)
    for i in range(hight-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol*width)
boxPrint('*', 5, 7)

# code to prin I
# *****
#   *
#   *
#   *
#   *
# *****


def printI(symbol, width, hight):
    print(symbol*width)
    for i in range(hight-2):
        print(' '*((width-1)//2)+symbol)
    print(symbol*width)


# printI('*', 5, 6)


# 1. # code to print piramid
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
def printprymid(symbol, v_length):    
    symbol=symbol+' '
    for i in range(v_length):
        print(symbol*v_length)
# printprymid('*', 5)

# print follwing pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# ******
def patt(symbol,l_len):
    symbol=symbol+' '
    for i in range (l_len):
        print (i*symbol)
# patt('*',7)

# 3# print full dimond
#     *
#    **
#   ***
#  ****
# *****
def full_dem(symbol,l_len):
    for i in range (l_len):
        i=i+1
        print(' '*(l_len-i)+symbol*i)
# full_dem('*',5)

# 4. # print following
# *****
#  ****
#   ***
#    **
#     *
def follw(symbol,l_len):
    symbol=symbol
    for i in range(l_len):
        print (' '*i+(l_len-i )*symbol)

# follw('*',5)

# sqp('*',7)

# 5 # code to print reverse
# *****
# ****
# ***
# **
# *

def rev(symbol, v_length):
    for i in range(v_length):
        k=v_length-i
        print(k*symbol)
        

# rev('* ', 5)


# print following pattern
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
def patt(symbol,l_len):
    for i in range(l_len):
        i=i+1
        print (' '*(l_len-i)+(symbol+' ')*i)
# patt('*',5)

# print following pattern
#     *
#    **
#   ***
#  ****
# *****
# *****
#  ****
#   ***
#    **
#     *

def patt(symbol,l_len):
    for i in range (l_len):
        i=i+1
        print(' '*(l_len-i)+symbol*i)
        if i ==5:
            for k in range(l_len):
                # k=k-1
                print(' '*k+symbol*(l_len-k))


patt('*',5)



def sqp(symbol, v_length):
    for i in range(v_length):
        print(symbol*i)



# code to print half dimond
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
def dem(symbol,l_len):
    for i in range(l_len):
        print (i*symbol)
        # print(i)
        if i==l_len-1:
            for i in range(l_len):
                k=l_len-i
                print(k*symbol)

# dem('*',6)

# print following line dymond
# *
#  *
#   *
#    *
#     *
def full_dem(symbol,l_len):
    for i in range(l_len):
        print(' '*i+symbol)

# full_dem('*',5)


# print following line dymond
#      *
#     *
#    *
#   *
#  *
def full_dem(symbol,l_len):
    for i in range(l_len):
        k=l_len-i
        print(' '*k+symbol)

# full_dem('*',5)










    