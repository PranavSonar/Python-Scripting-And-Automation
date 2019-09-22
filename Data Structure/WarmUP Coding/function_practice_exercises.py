# -*- coding: utf-8 -*-
"""Copy of 03-Function Practice Exercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wc-sK5becPQd1v_XkjMYBjgMT1mQ4INC

# Function Practice Exercises

Problems are arranged in increasing difficulty:
* Warmup - these can be solved using basic comparisons and methods
* Level 1 - these may involve if/then conditional statements and simple methods
* Level 2 - these may require iterating over sequences, usually with some kind of loop
* Challenging - these will take some creativity to solve

## WARMUP SECTION:

#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return a
        else:
            return b
    else:
        if a > b:
            return b
        else:
            return a

# Check
# print(lesser_of_two_evens(2,4))

# # Check
# print(lesser_of_two_evens(2,5))


"""#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
"""


def animal_crackers(text):
    text = text.split()
    if text[0][0].upper() == text[1][0].upper():
        return True
    else:
        return False

# Check
# print(animal_crackers('Levelheaded Llama'))

# # Check
# print(animal_crackers('Crazy Kangaroo'))


"""#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False
"""


def makes_twenty(n1, n2):
    if n1+n1 == 20 or n1 == 20 or n2 == 20:
        print(True)
    else:
        print(False)

# Check
# makes_twenty(20,10)

# # Check
# makes_twenty(2,3)


"""# LEVEL 1 PROBLEMS

#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
     
    old_macdonald('macdonald') --> MacDonald
    
Note: `'macdonald'.capitalize()` returns `'Macdonald'`
"""


def old_macdonald(name):
    return name[0].upper()+name[1:3]+name[3].upper()+name[4:]

# Check
# print(old_macdonald('macdonald'))


"""#### MASTER YODA: Given a sentence, return a sentence with the words reversed

    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
    
Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

    >>> "--".join(['a','b','c'])
    >>> 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

    >>> " ".join(['Hello','world'])
    >>> "Hello world"
"""


def master_yoda(text):
    return(' '.join(text.split()[::-1]))

# Check
# print(master_yoda('I am home'))

# # Check
# print(master_yoda('We are ready'))


"""#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    
NOTE: `abs(num)` returns the absolute value of a number
"""


def almost_there(n):
    if n in range(90, 110) or n in range(190, 210):
        return True
    else:
        return False


# Check
# almost_there(104)

# # Check
# almost_there(150)

# # Check
# almost_there(209)

"""# LEVEL 2 PROBLEMS

#### FIND 33: 

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
"""


def has_33(nums):
    print(nums)
    for i in range(len(nums)):
        if nums[i] == 3:
            if nums[i+1]==3:
                print (True)
                return True
            else:
                print(False)
                return False
        else:
            continue

#             # Check
# has_33([1, 3, 3])

# # Check
# has_33([1, 3, 1, 3, ])

# # Check
# has_33([3, 1, 3])

"""#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(text):
    newText=''
    for i in range(len(text)):
        newText+=text[i]*3
    print (newText)



# # Check
# paper_doll('Hello')

# # Check
# paper_doll('Mississippi')

"""#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
"""


def blackjack(a, b, c):
    sum=a+b+c
    if sum <=21:
        print (sum)
        return sum
    elif sum > 21 and 11 in (a,b,c):
        print (sum-10)
        return (sum-10)
    else:
        print ("BUST")
        return ("BUST")
# Check
# blackjack(5, 6, 7)

# # Check
# blackjack(9, 9, 9)

# # Check
# blackjack(9, 9, 11)

"""#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
 
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
"""


def summer_69(arr):
    sum=0
    for i in range(len(arr)):
        if arr[i] in range(6,10):
            pass
        else:
            sum+=arr[i]
    print(sum)
    return sum


# # Check
# summer_69([1, 3, 5])

# # # Check
# summer_69([4, 5, 6, 7, 8, 9])

# # # Check
# summer_69([2, 1, 6, 9, 11])

"""# CHALLENGING PROBLEMS

#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False
# """
def spy_game(nums):
    for i in range(len(nums)-3):
        return nums[i]==0 and 0 in nums[i:] and 7 in nums[i:]

# # Check
print(spy_game([1, 2, 4, 0, 0, 7, 5]))

# Check
spy_game([1, 0, 2, 4, 0, 5, 7])

# Check
spy_game([1, 7, 2, 0, 4, 5, 0])

"""#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
    count_primes(100) --> 25

By convention, 0 and 1 are not prime.
"""


def count_primes(num):
    pass


# Check
count_primes(100)

"""### Just for fun:
#### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
    print_big('a')
    
    out:   *  
          * *
         *****
         *   *
         *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. <br>For purposes of this exercise, it's ok if your dictionary stops at "E".
"""


def print_big(letter):
    pass


print_big('a')

"""## Great Job!"""
