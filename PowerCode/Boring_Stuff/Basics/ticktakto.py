import pprint
theboard={'T-L':'O','T-M':' ','T-R':' ',
          'M-L':' ','M-M':' ','M-R':'X',
          'B-L':' ','B-M':' ','B-R':' ',
        }
    
# print(theboard)

# pprint.pprint(theboard)
# theboard['M-R']=' '
# pprint.pprint(theboard)
# theboard['M-M']='O'
# pprint.pprint(theboard)
def printboard(board):
    print(board['T-L']+' | '+board['T-M']+' | '+board['T-R'])
    print('----------')
    print(board['M-L']+' | '+board['M-M']+' | '+board['M-R'])
    print('----------')
    print(board['B-L']+' | '+board['B-M']+' | '+board['B-R'])
printboard(theboard)
pprint.pprint(theboard)
print(type('abc'))