# This is a Gass the Number Game
import random

print('Hello.What is your name?')
name = input()

print("Well, "+name+' I am Thinking a number between 50 and 100.')
secretNumber = random.randint(50, 100)

for guessTaken in range(1, 5):
    print('Take a guess.')
    guessNumber = int(input())
    if guessNumber < secretNumber:
        print('You Guess is too low.')
    elif guessNumber > secretNumber:
        print('You Guess is too High.')
    else:
        break
if guessNumber == secretNumber:
    print('Great Job, '+name+'! You Guessed my Number correctly in ' +
          str(guessTaken)+' Guesses')
else:
    print('Oops ! You Have tried too many time, and the correct answer is '+str(secretNumber))
