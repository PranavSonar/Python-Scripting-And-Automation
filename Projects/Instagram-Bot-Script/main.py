# Command to install request library "pip install requests"
# import requests library to access the data from api url
import requests
# install before importing using "pip install urllib3"
import urllib

# For Sentiment Analysis in Python, we use the library TextBlob "pip install textblob"
from textblob import TextBlob

# For the test data,download the data set of TextBlob library: "python -m textblob.download_corpora"
from textblob.sentiments import NaiveBayesAnalyzer

# basic url of instagram to a connect the user
base_url = 'https://api.instagram.com/v1/'


def owner_info():
    owner_url = base_url+'users/self/?access_token='+app_access_token
    print "Owner Details Get Request Url: - " + owner_url
    owner_data = requests.get(owner_url).json()

    if owner_data['meta']['code'] == 200:
        if len(owner_data['data']):
            print "Owner Information Are Following : -"
            print "\t UserName : %s " % (owner_data['data']['username'])
            print "\t Full Name: %s " % (owner_data['data']['full_name'])
            # print "Bio : %s " % (owner_data['data']['bio'])
            print "\t Number of Post: %s " % (owner_data['data']['counts']['media'])
            print "\t you are Following: %s People. and %s People Following You on Instagram." % ((owner_data['data']['counts']['follows']), (owner_data['data']['counts']['followed_by']))
        else:   # if user date is not valid format
            print "User Does not Exist !-_-!"
    else:       # if any thing goes wrong
        print "Status Code Other than 200 Received. Something goes Wrong"


def get_user_id(insta_username):
    # search query url for  searching any keywords username from instagram
    search_url = (base_url + 'users/search?q=%s&access_token=%s') % (insta_username, app_access_token)
    print '\nSearch Query GET url of User Name: ' + insta_username + " is Following : \n" + search_url
    # store all search result into json format
    query_result = requests.get(search_url).json()
    if query_result['meta']['code'] == 200:
        if len(query_result['data']):
            # show the result of search query and select top one from the list
            print "\t User Name: %s \n\t User ID: %s" % (query_result['data'][0]['username'], query_result['data'][0]['id'])
            user_id = query_result['data'][0]['id']
            return user_id
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


def user_details(username):
    # call user name search and to convert into user id function
    specific_user_id = get_user_id(username)
    # make a specific user profile user_id AND access all details
    user_id_url = (base_url + 'users/%s?access_token=%s') % (specific_user_id, app_access_token)
    print '\nSelected user Profile Get Url is : %s' % user_id_url
    # store result of specific user id information
    user_info = requests.get(user_id_url).json()
    # it will show all details of specific user which will searched
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print "Searched User Information Are Following : -"
            print "\t UserName : %s " % (user_info['data']['username'])
            print "\t Full Name: %s " % (user_info['data']['full_name'])
            print "\t Profile Pic : %s " % (user_info['data']['profile_picture'])
            # print "\t Bio : %s " % (user_info['data']['bio'])
            print "\t Number of Post: %s " % (user_info['data']['counts']['media'])
            print "\t Following: %s  \n\t Followers %s" % ((user_info['data']['counts']['follows']), (user_info['data']['counts']['followed_by']))
        else:  # if user date is not valid format
            print "User Does not Exist !-_-!"
    else:  # if any thing goes wrong
        print "Status Code Other than 200 Received. Something goes Wrong"


# function for getting resent media post of owner
def get_own_post():
    get_self_media = base_url + 'users/self/media/recent/?access_token=' + app_access_token
    print "Get Recent Media Url: " + get_self_media
    recent_media = requests.get(get_self_media).json()
    if recent_media['meta']['code'] == 200:
        if len(recent_media['data']):
            image_name = recent_media['data'][0]['id'] + '.jpeg'
            image_url = recent_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
            return recent_media['data'][0]['id']
        else:
            print "There is no recent post!"
            return None
    else:
        print 'Status code other than 200 received!'


# function for getting resent media post of specific user post
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    get_self_media = base_url + 'users/' + user_id + '/media/recent/?access_token=' + app_access_token
    print "Get Recent Media Url: " + get_self_media
    recent_media = requests.get(get_self_media).json()
    if recent_media['meta']['code'] == 200:
        if len(recent_media['data']):
            image_name = recent_media['data'][0]['id'] + '.jpeg'
            image_url = recent_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            return recent_media['data'][0]['id']
        else:
            print "There is no recent post!"
            return None
    else:
        print 'Status code other than 200 received!'


# get post like list and like count
def get_like_list(insta_username):
    # media_id get by calling get_user_post Function
    media_id = get_user_post(insta_username)
    # generate like list url
    like_list_url = base_url + 'media/' + media_id + '/likes?access_token=' + app_access_token
    print "Media Like List Url :" + like_list_url
    like_list = requests.get(like_list_url).json()

    if like_list['meta']['code'] == 200:
        if len(like_list['data']):
            position = 1
            print "List Of People Who Like This Post :"
            for users in like_list['data']:
                if users['username'] != None:
                    print position, users['username']
                    position = position + 1
                else:
                    print "No one Has Like This Post Yet"
        else:
            print "User Does Not Have any post"
    else:
        print "Status code other than 200 received."


# Like a user Post
def like_a_post(insta_username):
    # media_id get by calling get_user_post Function
    media_id = get_user_post(insta_username)
    # it will make a url for like any post
    like_url = base_url + 'media/' + media_id + '/likes'
    payload = {"access_token": app_access_token}
    print 'Like Post URL: ' + like_url
    # send like to user post
    post_a_like = requests.post(like_url, payload).json()
    # check whether the like post Successfully or not
    if post_a_like['meta']['code'] == 200:
        print 'Like on post Successfully -_- .'
    else:
        print 'Your like was unsuccessful. Try again!!!'


# post a comment to user post
def post_a_comment(insta_username):
    # media_id get by calling get_user_post Function
    media_id = get_user_post(insta_username)
    # get user comment and store in comment_text Variable
    comment_text = raw_input("\nEnter Your Comment Here: \t")

    # check whether the Comment text is Correct Format and Size
    # The comment cannot consist of all capital letters.(it will convert into Capitalize case)
    comment_text = comment_text.capitalize()

    # The total length of the comment cannot exceed 300 characters.
    if len(comment_text) < 300:
        # combine comment text and app access token and make comment payload
        payload = {"access_token": app_access_token, "text": comment_text}
        # make comment url by using media ID
        comment_url = (base_url + 'media/%s/comments') % media_id
        print 'Posting Comment to URL : %s' % comment_url

        # posting Comment om Instagram
        make_comment = requests.post(comment_url, payload).json()

        # check whether the comments posted Successfully or not
        if make_comment['meta']['code'] == 200:
            print "\n\tSuccessfully Post a new comment! -_-.\n\n\n"
        else:
            print "\n\tUnable to add comment. Try again!\n\n\n"
    else:
        print "\n\tPlease Enter only Text 300 Alphabet's\n\n\n"


# Function For get All Comment List On any Post
def comment_list(insta_username):
    # media_id get by calling get_user_post Function
    media_id = get_user_post(insta_username)
    comment_list_url = base_url + 'media/' + media_id + '/comments?access_token=' + app_access_token
    print "Comment List Url : " + comment_list_url
    comment_list = requests.get(comment_list_url).json()

    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            position = 1
            print "List Of people Who Comment In This Post :"
            for _ in range(len(comment_list['data'])):
                if comment_list['data'][position-1]['text']:
                    print comment_list['data'][position - 1]['from']['username']+' said: ' + comment_list['data'][position - 1]['text']
                    position = position + 1
                else:
                    print 'No one had commented on Your post!\n'
        else:
            print "There is no Comments on User's Recent post.\n"
    else:
        print 'Status code other than 200 received.\n'


# function For Deleting negative Comment
def delete_negative_comment(insta_username):
    # media_id get by calling get_user_post Function
    media_id = get_user_post(insta_username)
    delete_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
    print 'Delete Comment url : %s' % delete_url
    comment_info = requests.get(delete_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            # Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                # Analysing the sentiments and gives the exact figure upto positivity or negativity..
                print blob.sentiment
                # Prints the sentiments and gives the exact figure upto positivity or negativity..
                if blob.sentiment.p_neg > blob.sentiment.p_pos:  # Checking condition for negative condition..
                    print 'Negative comment : %s' % comment_text
                    delete_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % ( media_id, comment_id, app_access_token)
                    print 'DELETE request url : %s\n' % delete_url
                    delete_info = requests.delete(delete_url).json()
                    # Fetching Json data after deleting the comment....

                    if delete_info['meta']['code'] == 200:  # Checking success code .....
                        print 'The Negative Comment From the Post has successfully deleted!\n'
                    else:
                        print 'Check Network issues , Unable to delete the comment!!\n'
                else:
                    print 'The Comment is Positive comment : %s\n' % comment_text
        else:
            print 'There are no existing comments on the post!\n'
    else:
        print 'Status code other than 200 received!\n'


# Function For action Call
def start_bot():
    while True:
        print '\nYou Can Perform Following Task By Using This App on Your Instagram Data.'
        print "\t1.Get your own details."
        print "\t2.Get details of a user by username."
        print "\t3.Get your own recent post."
        print "\t4.Get the recent post of a user by username."
        print "\t5.Get a list of people who have liked the recent post of a user."
        print "\t6.Like the recent post of a user."
        print "\t7.Get a list of comments on the recent post of a user."
        print "\t8.Make a comment on the recent post of a user."
        print "\t9.Delete negative comments from the recent post of a user."
        print "\t10.Exit"
        # ask user for Entering there respective task to do
        choice = raw_input("Enter you choice of Task To Do: ")

        # 1.Get your own details.
        if choice == "1":
            owner_info()

        # 2.Get details of a user by username.
        elif choice == "2":
            # ask user to enter any user name to find their details
            user = "\nif You Want to Search Specific user Details Please Enter User name: \t"
            username = raw_input(user)
            # call user information finder function
            user_details(username)

        # 3.Get your own recent post.
        elif choice == "3":
            get_own_post()

        # 4.Get the recent post of a user by username.
        elif choice == "4":
            # ask user to enter any user name to find their details
            user = "\nif You Want to Get any Specific User Recent Post Please Enter User name :\t"
            username = raw_input(user)
            # call user information finder function
            get_user_post(username)
            print 'User recent Media image has been downloaded!'

        # 5.Get a list of people who have liked the recent post of a user.
        elif choice == "5":
            # ask user to enter any user name to like there post
            user = "\nif You Want to Like any Specific User Recent Post Please Enter User name :\t"
            username = raw_input(user)
            get_like_list(username)

        # 6.Like the recent post of a user.
        elif choice == "6":
            # ask user to enter any user name to like there post
            user = "\nif You Want to Like any Specific User Recent Post Please Enter User name :\t"
            username = raw_input(user)
            # call user user post like function
            like_a_post(username)

        # 7.Get a list of comments on the recent post of a user.
        elif choice == "7":
            insta_username = raw_input("Enter the username of the user: ")
            comment_list(insta_username)

        # 8.Make a comment on the recent post of a user.
        elif choice == "8":
            # ask user to enter any user name to comment there recent post
            user = "\nPlease Enter User name :\t"
            username = raw_input(user)
            post_a_comment(username)

        # 9.Delete negative comments from the recent post of a user.
        elif choice == "9":
            # ask user to enter any user name to Delete comment there recent post
            user = "\nPlease Enter User name :\t"
            username = raw_input(user)
            delete_negative_comment(username)

        # Function For Terminate Program
        elif choice == "10":
            exit()

        # for any Wrong Input
        else:
            print "\n\t\t!!! Please Select a Valid Option !!! \n\n\n"


#  <------------App Start From Here---------------------------------------->
# Application Execution Start From Here
print '\nWelcome to Smart-Insta-Bot\n'
question = 'Would You Like to Use This App As Default Token ID : "1517125858.d5636d7.460b58d0dce14bd894f17a17d20fc80f" (Y/N): \t'
# Ask for token ID to User
token_option = raw_input(question)
if token_option.upper() == "Y":
    # instagram Default access token
    app_access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxenter your Acess tokenXXXXXXXXXXXXX'
    # set access token and call Start chat function to do multiple function
    start_bot()
elif token_option.upper() == "N":
    app_access_token = raw_input("Please Enter Instagram Access Token :\t")
    # check whether the access token is valid or not
    if len(app_access_token) > 10:
        # set access token and call Start chat function to do multiple function
        start_bot()
    else:
        print "\n!!! Access Token Not Valid. !!! \nPlease Enter a Valid Access Token and Try Again."
        exit()

else:
    print "please select only (y/n) and try again."
