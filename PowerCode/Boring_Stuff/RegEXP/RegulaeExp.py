import re
message= "Call me at 91-78370-55334 or call at 93-23333-54534 batabc tacbat batabc batxyz"
print (message)
phone_re=re.compile(r'\d\d-\d\d\d\d\d-\d\d\d\d\d')
phone=phone_re.findall(message)
print(phone[1])
phone_re_grp=re.compile(r'(\d\d)-(\d\d\d\d\d-\d\d\d\d\d)')
phone=phone_re_grp.search(message)
print(phone.group(2))
batreg=re.compile(r'bat(abc|xyz)')
fd=batreg.search(message)
print(fd[1])
print(phone_re_grp)
