#Single Player Guessing Game
#This game include a single user to guess a computer-generated number

#IMPORTS
import random

#VARIABLES
answer = -1
user_guess = -1
lives_counter = -1

#BEGIN GAME HERE
print ("Welcome to the single player guessing game.\n This is on the next line")
print("Guess a number between 1-100")

answer = random.randint(1,100)
print(answer)

print("What is your guess?")
user_guess=input("->")
print("your guess",user_guess)
while(lives_counter < 0):
if user_guess == answer :
     print("You Win")
elif user_guess > answer:
      print("Guess Lower")
elif user_guess > answer:
      print("Guess Higher")
else:
       print("An error has occured")
       print("Thanks for playing")
       print ("You have", lives_counter,"lives left.")
