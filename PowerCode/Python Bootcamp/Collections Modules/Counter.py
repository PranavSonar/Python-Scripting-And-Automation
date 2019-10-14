from collections import Counter

l = [1, 1, 2, 1,1,1,1,1, 2, 323, 2, 3, 4, 3, 4, 3, 'sad',
     'd', 'function', 'fd', 'f', 'd', 'r3', 43, 4, 3]

print(Counter(l))


s='dffdfsdasddfsd c fd'
print(Counter(s))


s='HOw mamy time word word show up in the scrtmg ggg,df,ffrrref dc'

c=Counter(s.split())

print(c.most_common(2).append('dd'))