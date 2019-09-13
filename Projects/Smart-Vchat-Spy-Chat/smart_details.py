# Import Date and time
from datetime import datetime

class vchat:
    # Constructor for initializing class
  def __init__(self, name, salutation, age, rating):
      self.name = name
      self.salutation = salutation
      self.age = age
      self.rating = rating
      self.is_online = True
      self.chats = []
      self.current_status_message = None
      self.chats_avg = [0,0]


# Default user for Smart vchat uses
defaultuser = vchat('Vivek Kumar', 'Mr.', 21, 4.7)
#
friend_one = vchat('Rony Roy', 'Mr.', 27, 4.9)
friend_two = vchat('Anindyo Bose', 'Ms.', 24, 4.39)
friend_three = vchat('Parmpreet Kaur', 'Ms.', 22, 3.95)
friend_four = vchat('Gaurav Singh', 'Dr.', 37, 4.5)
friend_five = vchat('Harry Glot', 'Ms.', 23, 4.95)

friends = [friend_one, friend_two, friend_three, friend_four, friend_five]


class ChatMessage:

  def __init__(self, message, sent_by_me):
      self.message = message
      self.time = datetime.now()
      self.sent_by_me = sent_by_me


# v_name = "Vivek Kumar"
# v_salutation = "Mr."
# v_age = 21
# v_rating = 4.5

# all details in the form of Dictonary
# vchat = {
#   'name': 'Vivek Kumar',
#   'salutation': 'Mr.',
#   'age': 21,
#   'rating': 4.7,
#   'is_online': True
# }
