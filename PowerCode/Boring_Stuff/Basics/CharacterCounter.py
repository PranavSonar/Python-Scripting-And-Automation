sent='Hello Babby How are you doing'
print(sent)
count={}
for character in sent:
    count.setdefault(character,0)
    count[character]=count[character]+1
    print (character)