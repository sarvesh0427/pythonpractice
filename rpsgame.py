"""
Rock-Paper-Scissors Game

This Python program is a simple Rock-Paper-Scissors game where:
- The user plays against the computer.
- The computer randomly chooses Rock, Paper, or Scissors.
-The game determines the winner based on the standard rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
-The user can play multiple rounds.
"""

import random

lst = ["rock","paper","scissor"]

user_score = 0
computer_score = 0

print("----Welcome to the game!!!----")
print("Press 'q' if you want to quit.")

while True:
    rand1 = random.randint(0,2)

    computer_pick = lst[rand1]
    user_pick = input("Rock, Paper or Scissor: ").lower()
    print(f"Computer pick {computer_pick}.")

    if (user_pick == "rock" and computer_pick == "scissor") or \
        (user_pick == "paper" and computer_pick == "rock") or \
        (user_pick == "scissor" and computer_pick == "paper"):
        print("You win !!!")
        user_score += 1
    elif user_pick == "q":
        break
    elif user_pick not in lst:
        print("Invalid!!!")
    elif user_pick == computer_pick:
        print("It's a tie.")
    else:
        print("Computer win !!!")
        computer_score += 1

print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")
