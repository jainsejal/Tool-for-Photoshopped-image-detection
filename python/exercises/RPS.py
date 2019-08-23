"""ROck, paper scissor game between user and computer"""
from random import randint
options = ["Rock", "Paper", "Scissor"]
message = {"tie": "Yawn it's a tie!", "win": "Yay you won!", "lost": "Aww you lost!"}
def decide_winner(user_choice, computer_choice):
  print "Your choice: %s" % (user_choice)
  print "System choice: %s" %(computer_choice)
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[1]:
    print message["lost"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["win"]
  elif user_choice == options[1] and computer_choice == options[2]:
    print message["lost"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["win"]
  elif user_choice == options[2] and computer_choice == options[0]:
    print message["win"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["lost"]
  else:
    print message["lost"]
  
def play_RPS():