# game.py
import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
if user_choice in ["rock", "paper", "scissors"]:
    print(user_choice)

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print(computer_choice)
  
    if user_choice == computer_choice:
        print("Your choices are the same. There is no winner.")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("The computer wins.")
        else:
            print("The user wins.")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("The computer wins.")
        else:
            print("The user wins.")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("The computer wins.")
        else:
            print("The user wins.")
else:
    print("User input is invalid")
    exit ()
