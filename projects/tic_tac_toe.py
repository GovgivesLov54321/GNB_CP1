# GNB - 1st - Tic Tac Toe
import random

while True:
    print("Welcome to Tic Tac Toe, User!")
    order = input("First, we'll figure out who is going first.\nChoose heads or tails for a coin flip (H or T):\n").strip().capitalize()
    
    coin_flip = random.randint(1,2)

    if order == "H" and coin_flip == 1:
        print("You start, User.")
    elif order == "T" and coin_flip == 2:
        print("You start, User.")
    elif order == "H" and coin_flip == 2:
        print("Computer will start.")
    elif order == "T" and coin_flip == 1:
        print("Computer will start.")
    else:
        print("Not an option.")
        break

   
    if coin_flip == 1:
        print("It's heads!")
    else:
        print("It's tails!")


    row_one = [1, 2, 3]
    row_two = [4, 5, 6]
    row_three = [7, 8, 9]
    print(f"{row_one} \n{row_two} \n{row_three}")

    ("You are X's, User. The computer is O's.")

    choice = int(input("Which spot do you want first?"))

    if choice == 1 :
        row_one[0] = "X"
        print(f"{row_one} \n{row_two} \n{row_three}")