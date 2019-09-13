a = [1, 0, 3, 5, 6, 4, 1, 34, 56, 434, 4, 5445, 5, 6,1,0,6]
# bubble short

count=0


def Bshort(a,count):    
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            count+=1
            b=count
            print(b)
            Bshort(a,b)
    return a
    
# print(Bshort(a,count))
# select tion short

a = [1, 0, 3, 5, 6, 4, 1, 34, 56, 434, 4, 5445, 5, 6,1,0,6]
# bubble short

def Sshort(a):
    
    count=0
    for i in range(len(a)):
        for k in range(i, len(a)):
            if a[i] > a[k]:

                temp = a[i]
                a[i] = a[k]
                a[k] = temp
                count+=1
    print("Result of Sshort \n",a,count)

Sshort(a)
