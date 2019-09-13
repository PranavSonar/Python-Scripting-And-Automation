a = [1, 23, 3, 45, 9, [1, '1bs', 66], 'abc']
# print (a[5][1][1])
# print(a[6][1])

animal = ['cat', 'dog', a]
if 'cat' in animal:
    print(animal[2][5][-1])
    print(len(animal))
    print(a[1:3])
    print(animal)
    abc = 'vivek'
    a[5][1]=a[5][1]+abc
    print(animal)
    b=animal[2]
    print (b[3:])
    del b[3:]
    print (b)
    c=a+b+animal*20
    print (c)
    
    if 23 in c:
        print ('hi')
