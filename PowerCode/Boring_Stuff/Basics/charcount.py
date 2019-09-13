import pprint
message = '''Use the get method to print the value of the "model" key of the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
)
'''
count_char = {}
for char in message.upper():
    # print(char)
    count_char.setdefault(char,0)
    count_char[char]=count_char[char]+1
# pprint.pprint (count_char)
print(pprint.pformat(count_char['R']))