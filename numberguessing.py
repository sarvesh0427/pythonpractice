# number guessing game

import random

def guess_game():
    a = int(input("Enter lower range: "))
    b= int(input("Enter higher range: "))

    guess =0

    rand1 = random.randint(a,b)

    while True:
        guess += 1
        user_guess = int(input("Guess the number: "))
        if a<= user_guess <= b:
            if user_guess == rand1:
                print("You're correct")
                break
            elif user_guess > rand1:
                print("You're above the number.")
            else:
                print("You're below the number.")
        else:
            print(f"Please select the number in between {a} and {b}.")

    print(f"You guess the number in {guess} attempt.")

guess_game()