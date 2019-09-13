name = ['abc', 'vivek', 'xyz']
a, b, c = name
print(a, b)

a = 'acxx'
b = 'cbx'
c = 'sdcdjcnd'
abc=[a,b,c]
print(abc)
print(type(abc))
print (a in abc )
for b in abc:
  print ("Hello")

print(abc)
list=[m*2 for m in range(1,8)]
print(list)
del(list[1])
print(list)
print(a)
abc.append({'21'})
print(abc)
abc.extend(list)
print(abc)
print(abc.index(14))
abc.insert(5,list)
print(abc)
print(abc.pop())
print(abc)
abc.remove(list)
print(abc)
abc.reverse()
print(abc)
list.sort()
print(list)

tup=0,12233,5,
print(tup)
print(type(tup))
print(tuple(abc))
tup+=tuple(abc)
print(tup)


t={}
abc={1,3}
print(type(abc))
num={1,2,3,3,4,2,34,3,34}
print(num > abc)
abc={3:1,1:3}
print(abc)
r=dict(a=abc,b=abc)
print(r)
r['a']=45
print(r)
print(len(r))
print(r.keys())
print(r.values())
print(r.items())
for k,b in r.items(): 
  print (k,b)

print ([x for x in range(10)])
ax=[n*10 for n in range(10)]
st="i am 23 by 32 abd uiihi1"
print(''.join([n for n in st if n.isnumeric()]))
a=[1,233,44,4,54,5,5,6,56,676,77234,34,22,444]
print([p for p,q in enumerate(a) if q>20])

x = [dog for dog in 'pig']
print(x)

weights = {'a':3, 'b':5, 'c':7}
print(dir(weights))
print(weights)