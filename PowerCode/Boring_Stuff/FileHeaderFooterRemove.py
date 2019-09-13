import sys,os
filename='test.txt' 
fp = open(filename, 'r')

linenumber=0
header_row=2
footerrow=3
for line in fp.readlines():
    # print (line)
    linenumber=linenumber+1
    # print(linenumber)
    for line in range(header_row):
        print (line)