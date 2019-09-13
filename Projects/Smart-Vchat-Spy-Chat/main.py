# importing Old Data from smart details file
from smart_details import vchat, ChatMessage, defaultuser, friends
# Steganography python library added by running "pip install steganography"
# steganography library importing
from steganography.steganography import Steganography
# importing Date and time for Storing Date and of Message send and recive
from datetime import datetime
# import colored to view different Colored output "pip install colored --upgrade"
from colored import fg, bg, attr
# print ('%s%s Hello World !!! %s' % (fg(1), bg(15), attr(0)))

# Import easygui to View output on GUI Mode "pip install easygui"
import easygui
# easygui.msgbox("Welcome To Smart Chat App", 'Welcome to Python World')
# Code To Show output In GUI Mode

easygui.msgbox("<:---------------------------------------------------------------------:>\n<:------- Hello! Welcome to S         T. Let\'s get started ------------:>\n                             M       A                                   \n                              A     H                                    \n                               R   C                                     \n                                T V                                      \n<:---------------------------------------------------------------------:>", "Welcome to Smart VChat", ("Continue"))
easygui.msgbox("Now You Can Able To Chat With Your Friend With Highly Secure Way, Without worrying About your Privacy \n\n\n\t\t\t Developed By Vivek Kumar.", 'Smart VChat' , ("Let\'s Start Smart VChat"))

# easygui.msgbox('Developed By Vivek Kumar.', 'Smart VChat')
# easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))
# easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))

# predefinded STATUS_MESSAGES
STATUS_MESSAGES = ['Online', 'Offline', 'Happy Happy ...', 'Common On You Can Do it.', 'And So, It Begains ...',]

# importing CSV to save ChatMessage
import csv
# #csv code for write to CSV file
# with open('friends.csv', 'wb') as friends_data:
#     writer = csv.writer(friends_data)
#     writer.writerow([vchat.name, vchat.saluation, vchat.rating, vchat.age, vchat.is_online])

#csv code for data read from csv files
# with open('friends.csv', 'rb') as friends_data:
#     reader = csv.reader(friends_data)
#     for row in reader:
#         print row

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)
        for row in reader:
            friend = vchat(row[0], row[1], int(row[2]), float(row[3]))
            friends.append(friend)

# Start Smart Vchat All Features
def start_chat(defaultuser):
    current_status_message = None
    show_menu = True
    # Show the app all Features
    while show_menu == True:
        print "%s%s\nYou can perform Following task using Smart Chat.      " % (fg(41), bg(161))
        menu_options = "               1. Add a status update                 \n               2. Add a friend                        \n               3. Select a Friend                     \n               4. Send a secret message               \n               5. Read a secret message               \n               6. Read Chats from a user              \n               7. Close Application                   \n\n%s" %attr(0)
        #  get the menu_options from user
        menu_choices = raw_input(menu_options+"Please Enter Your Choice: \t")
        # validate the menu_options
        if menu_choices > 0 :
            # to convert other data type into interger Data type
            menu_choices = int(menu_choices)
            # if user select Add Status message
            if menu_choices == 1 :
                print "\nYour Have Selected Add a Status Feature. \n"
                current_status_message = add_status(current_status_message)

            #  if user select add_friend
            elif menu_choices == 2 :
                print "\nYour Have Selected Add a Friend Feature. \n"
                number_of_friends = add_friend()
                print "You have Now %d Friends in Friend List.\n" %(number_of_friends)

            #  if user want to Select a Friends
            elif menu_choices == 3 :
                print "\nYour Have Selected Select Friend Feature. \n"
                # code for Selecting Friends Come under this
                select_friend()

            #  if user want to send a secrat message
            elif menu_choices == 4 :
                print "\nYour Have Selected Send a Secrat Message Feature. \n"
                # code for Send a Secret Message Comes under this
                send_message()

            #  if user want to read a Secrat Massage
            elif menu_choices == 5 :
                print "\nYour Have Selected Read A Secrat Message Feature. \n"
                # Code for read a Secret message Comes under this
                read_message()

            # if user want to Read a Message
            elif menu_choices == 6 :
                print "\nYour Have Selected Chat Read Feature. \n"
                # code for Read a Chat From the user Comes here

            #  if user want to Close the App
            elif menu_choices == 7 :
                print "\nYour Have Selected Close Application. \n"
                close_application = "Are You Sure. (Y/N) \t"
                close = raw_input(close_application)
                # if user sure to close the app
                if close.upper() == "Y" :
                    show_menu == False
                    exit()
                else :
                    show_menu == True

            # if user select invalid options
    else :
        print "\t Select A Valid options"


# Add Status Massage Function Define here
def add_status(current_status_message):
    updated_status_message = None
    # check for anything is presented in current user status Massage
    if defaultuser.current_status_message != None:
      print "Your current status message is " + defaultuser.current_status_message + "\n"
    else:
      print 'You don\'t have any status message currently \n'

    default = raw_input("\nDo you want to select from the older status (y/n)? \t")
      # if user want to set new status Massage
    if default.upper() == "N":
          new_status_message = raw_input("Write a New Status Massage: \t")
          if len(new_status_message) > 0:
              # Add New Status massage into old Status Massage list
              STATUS_MESSAGES.append(new_status_message)
              # update the STATUS_MESSAGES
              updated_status_message = new_status_message
              print "Now Your status is : ' " + updated_status_message + " '\n"
              defaultuser.current_status_message = updated_status_message
          else:
             print "Please Enter a Valid Status Update."
    elif default.upper() == "Y" :
        item_position = 1

        for message in STATUS_MESSAGES:
            # to Print All Available Status message
            print str(item_position) + ". " + str(message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above Status: \t "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    else:
        print "Press Y or N only."
    if updated_status_message:
        print "\nNow Your status is ' " + updated_status_message + " ' \n"
        defaultuser.current_status_message = updated_status_message
    else:
        print "You current don't have a status update"


# Add A Friends Function
def add_friend():
    # initializing defaultuser object with none value
    new_friend = vchat ('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: \t")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: \t")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input(new_friend.name+"\'s Age? \t")
    #coverting input data to integer format
    new_friend.age = int (new_friend.age)

    new_friend.rating = raw_input(new_friend.name+"\'s Smart rating? \t")
    #converting input data into float
    new_friend.rating = float(new_friend.rating)

    # check for valid input details intered by the user regarding his friend or not
    if len(new_friend.name)>0 and new_friend.age > 12 and new_friend.rating >= 1:
        try:
            with open("friends.csv", 'ab') as friends_data:
                write = csv.writer(friends_data)
                write.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating])
        except:
            print 'File not available'
        friends.append(new_friend)
        print '\nNew Friend Name " %s " Age " %d " of Rating " %.2f " Added into Friend List.' %(new_friend.name, new_friend.age, new_friend.rating)
    else:
        print '\nSorry! Invalid entry. We can\'t add Smart with the details you provided'
    return len(friends)

# select_friend a Friend Function
def select_friend():
    def view_friend():
        item_number = 0
        # it will select all the friend from friend list and print a list of all friends details
        for friend in friends:
            print '\t%d. %s Age %d Rating %.2f is Online' % ((item_number + 1), friend.name, friend.age, friend.rating)
            item_number = item_number + 1
    view_friend()
    # get an idevedual friend from the list
    friend_choice = raw_input("\nSelect a Friend from your Friends List: \t")
    friend_choice_position = int(friend_choice) - 1
    #return selected friend number
    return friend_choice_position

# send a Secret message Function start from here
def send_message():
    friend_choice = select_friend()
    original_image = raw_input("In Which Image File You Want to Hide Your Message? (Enter Image File Name without Any extension Like .jpg) \t") + '.jpg'
    text = raw_input("Type Your Secure Message Now: \t")
    Secured_image = raw_input("Enter Name (without extension .jpg) For Newly Generated Secure Message File : \t")
    #set the name for the out secure image with text
    output_path = Secured_image + '.jpg'
    Steganography.encode(original_image, output_path, text)
    #split text message to check any special message involved or not
    temp = text.split(' ')
    #If a Smart send a message with special words such as SOS, SAVE ME etc. you should display an appropriate message
    special = ['SOS', 'sos' 'Help', 'help', 'HELP', 'Save', 'SAVE', 'save']
    for any in special:
        if any in temp:
            temp[temp.index(any)] = ' Please Help Me. i am In Denger. Contact me as soon as Possible'
    #replece with new full length message
    text = str.join(' ', temp)
    # store Date and Time
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[friend_choice].chats.append(new_chat)
    print '\n\tYour secret message is ready! in File " %s "' %output_path

# read a Secret message Function
def read_message():
    sender = select_friend()
    output_path = raw_input("\nEnter the Secure Image File Name (without any extension Like .jpg) To Read Your Secure Message: \t")+".jpg"
    try:
        secret_text = Steganography.decode(output_path)
    except ValueError:
        print "\tNo Any Secret Message In This Image. Please Try Another Image File \n"
        read_message()
    # show the Secrate message
    print 'The Secret message For You "'+ secret_text +' ".'
    # store Date and time
    # new_chat = {
    #     "message": secret_text,
    #     "time": datetime.now(),
    #     "sent_by_me": False
    # }
    #
    # friend[sender]['chats'].append(new_chat)
    # print "Your secret message has been saved!"


# Main program Start from Here
# welcome Massage Printing
# print ('%s%s Hello World !!! %s' % (fg(1), bg(15), attr(0)))
print '%s%s<:---------------------------------------------------------------------:>' % (fg(85), bg(1))
print '<:------- Hello! Welcome to S         T. Let\'s get started ------------:>'
print '                             M       A                                   '
print '                              A     H                                    '
print '                               R   C                                     '
print '                                T V                                      '
print '<:---------------------------------------------------------------------:>%s' %(attr(0))

#  ask user to select as old user or not
question = "\nContinue as " + defaultuser.salutation + " " + defaultuser.name + "(Y/N)? \t"
existing = raw_input(question)

# check whether user want to Continue as old user or a new user
if existing.upper() == 'Y':
    # Some Code to User start as old user
    defaultuser.name= defaultuser.salutation + ' ' + defaultuser.name
    print "\nWelcome " + defaultuser.name + ". Glad to have you back with us."
    AskForPassword = defaultuser.name + " Please Enter your password: \t"
    password = raw_input(AskForPassword)
    #  check and verify password here
    if password == "" :
        #  print "Authentication complete. Welcome " + vchat.name + " age: " + str(vchat.age) + " and rating of: " + str(vchat.rating) + " Proud to have you onboard"
        print "\nAuthentication Complete. Welcome %s Age: %d and Rating of: %.1f Proud to have you onboard." % (defaultuser.name, defaultuser.age, defaultuser.rating)
        print "Now You Can Start Chat with your Friends."
        #  after all varifaction chat will start from here as a old user
        start_chat(defaultuser)
    # if user Enter Wrong password
    else:
        print "\n\t Please Enter Correct password. and Try again"
        easygui.msgbox("Please Enter Correct password", 'password Issue', ("Close"))

#  if a new user(not want to start as a old User) want to srart using Smart Vchat
elif existing.upper() == "N":
    #  if a new user(not want to start as a old User) want to srart using Smart Vchat app then first it create an empty object
    newuser = vchat('','',0,0.0)
    #  get user input "Name" and Salutation"
    newuser.name = raw_input("\nYou must tell me your Smart Name First: \t")
    # condition to check whether name Entered or not

    if len(newuser.name) > 0:
        #  print User name with Greetings
        newuser.salutation = raw_input("Should I call you (Mr. or Ms.) ? \t")
        #  Concanationation Name with Salutation
        newuser.name = newuser.salutation + ' ' + newuser.name
        print "Alright " + newuser.name + ". I\'d like to know a little bit more about you before we proceed..."
        # get user Age Information
        newuser.age = input("What is your age? \t")
        # condition to check and verify user age group
        if newuser.age > 12 and newuser.age < 50:
            # get user ranting
            newuser.rating = input("What is your Smart Rating? \t")
            if newuser.rating > 4.5 :
                print 'Great ace!'
            elif newuser.rating > 3.5 and newuser.rating <= 4.5 :
                print 'You are one of the good ones.'
            elif newuser.rating > 2.5 and newuser.rating <= 3.5 :
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            newuser.is_online = True
            #  print "Authentication complete. Welcome " + vchat.name + " age: " + str(vchat.age) + " and rating of: " + str(vchat.rating) + " Proud to have you onboard"
            print "\nAuthentication Complete. Welcome %s Age: %d and Rating of: %.1f Proud to have you onboard." % (newuser.name, newuser.age, newuser.rating)
            print "\t Now You Can Start Chat with your Friends."
            #  after all varifaction chat will start from here as a old user
            start_chat(newuser)
        # if Wrong Age group try to enter
        else:
            print "\t Sorry you are not of the correct age to be a Smart VChat User"

    # if smart user not enter there Valid name
    else:
        print "\t A Smart User needs to have a valid name. Try again please."

# if user try to enter wrong Input to the program
else:
    print "\t Please Select Only (Y/N) and Try Again"
