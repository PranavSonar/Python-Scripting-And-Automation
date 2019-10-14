# Step1: Get sentence to encryption
# sentence=str(input("Enter The Text :").strip())
sentence="My name is vivek kumar. i love india.my phone number is 7837098835 123456789 456"
# sentence="Vivek applew apple"
# Step2: split sentence into word
words=sentence.split()

# it will convert word to new word based on there passed parameter
def getWordEx(word,Exp):
  new_word=''
  for i in word:
    # a-->97
    # z-->122
    if i.isalpha() and i.islower():
      # add int+length
      # check if letter enc latter is greater then max alph
      if int(ord(i)+int(Exp)) not in range(97,122):
        i=chr(96+(int(ord(i)+int(Exp))-122))
      else:
        i=chr(ord(i)+int(Exp))
      new_word+=i
    # A-->65
    # Z-->90
    elif i.isalpha() and i.isupper():
      # add int+length
      # check if letter enc latter is greater then max alph
      if int(ord(i)+int(Exp)) not in range(65,90):
        i=chr(64+(int(ord(i)+int(Exp))-90))
      else:
        i=chr(ord(i)+int(Exp))
      new_word+=i
    # if word contaning number
    elif i.isdigit():
      # if digit found then make it in range   
      if int(i)+int(Exp) not in range(0,9):
        i=int(int(i)+int(Exp))%9
      else:
        i=int(i)+int(Exp)
      new_word+=str(i)
    else:
      new_word+=str(i)  
  return new_word


    



enc_words=''
for word in words:
  # Step3: check if word start with vowel and word length is even then add 1 integer value to each of the letter and form new words
  if word[0] in 'aeiou':
    if len(word)%2==0:
      word=getWordEx(word,1)
    else:
    # Step4: check if word start with vowel and word length is not even then add length of word values integer to each of the letter and form new words
        word=getWordEx(word,len(word))

  else:
      # Step4: check if word Not start with vowel then add multiple word length by 2 and add total to each of the letter and form new words
      word=getWordEx(word,2*len(word))
  enc_words+=str(word)+' '
  
  
print(sentence)
print (enc_words)


    
    



