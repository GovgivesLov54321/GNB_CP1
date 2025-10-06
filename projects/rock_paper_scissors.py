# GNB - 1st - 🔨 Rock, Paper, Scissors
import random
while True:
    user_choice = input("Choose rock, paper, or scissors:").strip().lower()

    if user_choice == "rock":
        print("User chooses: Rock!")
    elif user_choice == "paper":
        print("User chooses: Paper!")
    elif user_choice == "scissors":
        print("User chooses: Scissors!")
    else:
        print("Invalid input")
        continue

    comp_choice = random.randint(1,4)

    if comp_choice == 1:
        print("Computer chooses: Rock!")
    elif comp_choice == 2:
        print("Computer chooses: Paper!")
    else:
        print("Computer chooses: Scissors!")

    while True:


        if user_choice == "rock" and comp_choice == 1:
            print("It's a draw!")
        elif user_choice == "paper" and comp_choice == 2:
            print("It's a draw!")
        elif user_choice == "scissors" and comp_choice == 3:
            print("It's a draw!")
            continue
    while True:
        if user_choice == "paper" and comp_choice == 1:
            print("User wins!")
        elif user_choice == "rock" and comp_choice == 3:
            print("User wins!")
        elif user_choice == "scissors" and comp_choice == 2:
            print("User wins!")
        
        elif comp_choice == 1 and user_choice == "scissors"
        continue
