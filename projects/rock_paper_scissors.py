# GNB - 1st - 🔨 Rock, Paper, Scissors
import random


start = input("Hello, User. Would you like to play rock, paper, scissors against a computer? (Yes or No):\n").strip().capitalize()

if start == "Yes":
    
    user_points = 0
    comp_points = 0

    while True:    

        user_choice = input("Choose rock, paper, or scissors (say quit to stop game):\n").strip().lower()
        
        

        if user_choice == "rock":
            print("User chooses: Rock!")
        elif user_choice == "paper":
            print("User chooses: Paper!")
        elif user_choice == "scissors":
            print("User chooses: Scissors!")
        elif user_choice == "quit":
            print(f"Final score is: (Comp){comp_points} - (User){user_points}")
            if comp_points > user_points:
                print("Haha!!! You lost!!! 🤡")
            elif comp_points < user_points:
                print("Great job, Mr/Mrs Winner! 👑🥇")
            else:
                print("Nice try, User! It's a draw though.")
            break
        else:
            print("Invalid input")
            continue

        comp_choice = random.randint(1,3)

        if comp_choice == 1:
            print("Computer chooses: Rock!")
        elif comp_choice == 2:
            print("Computer chooses: Paper!")
        else:
            print("Computer chooses: Scissors!")

        if user_choice == "paper" and comp_choice == 1:
            print("User wins!")
            user_points += 1
            if True:
                print(f"Score is: (Comp){comp_points} - (User){user_points}")
        elif user_choice == "rock" and comp_choice == 3:
            print("User wins!")
            user_points += 1
            if True:
                print(f"Score is: (Comp){comp_points} - (User){user_points}")
        elif user_choice == "scissors" and comp_choice == 2:
            print("User wins!")
            user_points += 1
            if True:
                print(f"Score is: (Comp){comp_points} - (User){user_points}")

        elif comp_choice == 1 and user_choice == "scissors":
            print("Computer wins!")
            comp_points += 1
            if True:
                print(f"Score is: (Comp){comp_points} - (User){user_points}")
        elif comp_choice == 2 and user_choice == "rock":
            print("Computer wins!")
            comp_points += 1
            if True:
                print(f"Score is: (Comp){comp_points} - (User){user_points}")
        elif comp_choice == 3 and user_choice == "paper":
            print("Computer wins!")
            comp_points += 1
            if True:
                print(f"Score is: (Comp){comp_points} - (User){user_points}")
                
        elif user_choice == "rock" and comp_choice == 1:
            print("It's a draw!")
            if ("It's a draw!"):
                print(f"Score is: (Comp){comp_points} - (User){user_points}")
        elif user_choice == "paper" and comp_choice == 2:
            print("It's a draw!")
            print(f"Score is: (Comp){comp_points} - (User){user_points}")
        elif user_choice == "scissors" and comp_choice == 3:
            print("It's a draw!")
            print(f"Score is: (Comp){comp_points} - (User){user_points}")
        continue

elif start == "No":
    print("Ok. Leave then... 😒")
else:
    print("Not an option, buddy...")