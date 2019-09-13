import webbrowser
import sys
import pyperclip

# it will take input as an extra parameter or clipboard text
def get_arg():
    # take from extra parameter
    arg = sys.argv
    if len(arg) > 1:
        arg = ' '.join(arg[1:])
    else:
        # take from clipboard
        arg = pyperclip.paste()
    return(arg)


while True:
    # take input as direct input
    text = input("Search Text Plz : \t")
    if len(text) < 1:
        # if input not passed take from clipboard text/extra parameter
        arg = get_arg()
        # arg = pyperclip.paste()
    else:
        arg = text
    # shows available tasks and take option
    option = input(
        '''Please Select Operation On Google : 
                1. SEARCH 
                2. IMAGES
                3. YOUTUBE
                4. Maps
                5. FACEBOOK
                6. LINKEDIN
                7. GMAIL
                0.EXIT 
            \n\t''')
    option = option.upper()

    # matches option with multiple strings
    if option in ('0', 'EXIT', 'E', 'T', 'O', 'X'):
        print("You Have Selected : "+option)
        print("It's an Exit Request.")
        # if its for exit terminate the program
        exit()

    # for text search
    elif option in ('1', 'SEARCH', 'S', 'G'):
        option = 'SEARCH'.title()
        print("You Have Selected : "+option + " \nFor Input :" + arg)
        webbrowser.open('https://www.google.com/search?q='+arg)

        # for images search
    elif option in ('2', 'IMAGES', 'I', 'P', 'PHOTO'):
        option = 'IMAGES'.title()
        print("You Have Selected : "+option + " \nFor Input :" + arg)
        webbrowser.open('http://www.google.com/search?q=%s&tbm=isch' % arg)

        # for YOUTUBE videos search
    elif option in ('3', 'VIDEOS', 'V', 'YOUTUBE', 'Y', 'M', 'VIDEO', 'MOVIE'):
        option = 'YOUTUBE VIDEOS'.title()
        print("You Have Selected : "+option + " \nFor Input :" + arg)
        webbrowser.open(
            'https://www.youtube.com/results?search_query=%s' % arg)

    # for google maps
    elif option in ('4', 'MAPS', 'M', 'L'):
        option = 'MAPS'.title()
        print("You Have Selected : "+option + " \nFor Input :" + arg)
        webbrowser.open('https://www.google.com/maps/search/'+arg)

    # for google books
    elif option in ('5', 'FACEBOOK', 'FB', 'F'):
        option = 'FACEBOOK'.title()
        webbrowser.open('https://www.facebook.com/')
        print("You Have Selected : "+option)
    # for linkedin
    elif option in ('6', 'LINKEDIN', 'LN', 'L'):
        option = 'LINKED IN'.title()
        webbrowser.open('https://www.linkedin.com/mynetwork/')
        print("You Have Selected : "+option)
    # for gmail
    elif option in ('7', 'GMAIL', 'GM', 'M', 'MAIL'):
        option = 'GMAIL'.title()
        webbrowser.open('https://mail.google.com/mail/u/0/')
        print("You Have Selected : "+option)
    else:
        print("Kindly Select from avalible Option. You Have Entered : "+str(option))
