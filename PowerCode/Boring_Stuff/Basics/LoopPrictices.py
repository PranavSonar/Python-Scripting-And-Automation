# print ("Hello")


# for a in range(1,13):
#     print ('hello'+str(a))

import copy
name = ['Rahul', 'vivek', 'pram', 'abc']
a, b, c = 1, 2, 4
for i in range(len(name)):
    print('At Position '+str(i)+' IS '+name[i])
    print(a, b, c)
    a, b, c = c, b, a
    print(a, b, c)
c += 2
a -= 4
b *= 3
b /= 100

print(a, b, c)
print(name.index('vivek'))
print(name[1])
print(name)
name.append('shashank')
print(name)
name.insert(4, 1)
print(name)
name.reverse()
print(name)
name.remove('abc')
print(name)
del name[1]
name.sort(reverse=True)
print(name)
name.append('cc')
name.append('FF')
name.append('zz')
name.append('ZZ')
name.sort()
print(name)
name.sort(key=str.upper, reverse=True)
print(name)


a = 'Hello'
for i in range(len(a)):
    print(i)
    print(a[i])

if 'Hel' in a:
    print(a)

print(a.replace('l', str(4)))
# print (a[2:])
b = a
print(b)
a = a.replace('l', str(4))
print(a)

print(name)
dev = name
print(dev)
dev = ['aa', 'bb']
print(dev)
name.append('pop')
print(name)
print(dev)
devlop = copy.deepcopy(name)
print('-------------------------------------')
print(devlop)
print(name)
name.append('fuck')
print(devlop)
print(name)


listname = ['hi',
            'hello',
            'jdj',
            'sdad']
a ='av'+\
'cd'
print(listname)

print(a)
