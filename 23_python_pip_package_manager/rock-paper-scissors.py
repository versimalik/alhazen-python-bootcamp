from random import randint
from stringcolor import *

print('Rock-Paper-Scissor Game')
print('=======================')

weapon = ['rock', 'paper', 'scissor']
computer = weapon[randint(0,2)]

print("What weapon do you want to use?")
print("👊 / 🤚 / ✌")
player = input().lower()

if player == computer:
  print(f"Player and Computer use {player}")
  print(cs("Nobody wins!", "grey"))
elif player == 'rock':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'paper':
    print(cs("Computer wins!", "red"))
    print("Paper covers Rock")
  elif computer == 'scissor':
    print(cs("Player wins!", "green"))
    print("Rock smashes Scissor")
elif player == 'paper':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'rock':
    print(cs("Player wins!", "green"))
    print("Paper covers Rock")
  elif computer == 'scissor':
    print(cs("Computer wins!", "red"))
    print("Scissor cuts Paper")
elif player == 'scissor':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'rock':
    print(cs("Computer wins!", "red"))
    print("Rock smashes Scissor")
  elif computer == 'paper':
    print(cs("Player wins!", "green"))
    print("✌ cuts ✋")
else:
  print("You input an invalid weapon!")