abc='Hello\t\n Baby\\"s b\ty'
# print(abc)
xy=r'fhdfvdsknmvd\dweor43irt34r3\erwo=r43rjfsd;vfs\dfd\t\nre'
# print (xy)
mess=r"""fucscjsd
dsahdsf
fdsf\n
wed\t\ndw37rew]d
w]\\]x\\NNDSAz"""
# print (mess)
me1='''swsdwsdewcrec
dsc
sdfc
ef
ds
fdsf
edf
df'''
# print(me1)



test='Hello World'
# print(test[4:8])



t1='Hi bodddy'
# print(t1.upper().lower().isupper())

h1="Abc1"
print(h1.isalnum())
print(h1.lower().title())
print(h1.lower().startswith('a'))
print(h1.endswith('c'))
print("vivek".join([abc,h1]))


test1='Hello Buddy'
print('_'.join(test1))
print(test1.split())
t2=test1.rjust(20,"|")
print(t2)
print(t2.lstrip('|'))
print(t2.replace('|','vivek'))

import pyperclip
# print(pyperclip.copy(t2))
print(pyperclip.paste())
