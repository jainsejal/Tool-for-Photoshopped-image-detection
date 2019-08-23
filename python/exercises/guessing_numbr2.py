# Game based on guessing the number
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
# Start your game!
print "Your limit for guessing is from 1 to 10" 
#Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
while guesses_left > 0:
  guess = int(raw_input("Your guess:"))
# if guesses are same as the random number then print the the message
  if guess == random_number:
    print "You win"
# exit the loop and if guess is not equal decrement the guesses left and again go through the loop    
    break
  guesses_left -= 1
# after all the guesses are done and then also random number is not being guessed print the other message
else:
  print "You lose"
  
"""o/p: Your limit for guessing is from 1 to 10
Your guess:5
Your guess:8
Your guess:8
You lose """  