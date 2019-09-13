student={'name':'vivek','type':'eng','level':2}

print (student.values())
print(student.items())
print(student.keys())

for i , k in student.items():
    print (i,k)

if 'vivek' in student.values():
    print (student.keys())

print (student.get('type','oo'))