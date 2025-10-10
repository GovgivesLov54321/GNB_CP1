# GNB - 1st - Tic Tac Toe
import random

print("Welcome to Tic Tac Toe, User!")
order = input("First, we'll figure out who is going first:\nChoose heads or tails for a coin flip (H or T):\n").strip().capitalize()

row_one = [1, 2, 3]
row_two = [4, 5, 6]
row_three = [7, 8, 9]

while True:   
    coin_flip = random.randint(1,2)

    ("You are X's, User. The computer is O's.")
   
    comp_choice = random.randint(1,9)

    if order == "H" and coin_flip == 1:
        if coin_flip == 1:
            print("It's heads!")
        else:
            print("It's tails!")
        print("You start, User.")
        print(f"{row_one} \n{row_two} \n{row_three}") 
        user_choice = int(input("Which spot do you want first?"))
        if user_choice == 1 :
            row_one[0] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 2 :
            row_one[1] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 3 :
            row_one[2] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 4 :
            row_two[0] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 5 :
            row_two[1] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 6 :
            row_two[2] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 7 :
            row_three[0] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 8 :
            row_three[1] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 9 :
            row_three[2] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        else:
            print("Not an option, bud.")
            break
    elif order == "T" and coin_flip == 2:
        if coin_flip == 1:
            print("It's heads!")
        else:
            print("It's tails!")
        print("You start, User.")
        print(f"{row_one} \n{row_two} \n{row_three}")
        user_choice = int(input("Which spot do you want first?"))
        if user_choice == 1 :
            row_one[0] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 2 :
            row_one[1] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 3 :
            row_one[2] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 4 :
            row_two[0] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 5 :
            row_two[1] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 6 :
            row_two[2] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 7 :
            row_three[0] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 8 :
            row_three[1] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif user_choice == 9 :
            row_three[2] = "X"
            print(f"{row_one} \n{row_two} \n{row_three}")
        else:
            print("Not an option, bud.")
            break

    elif order == "H" and coin_flip == 2:
        if coin_flip == 1:
            print("It's heads!")
        else:
            print("It's tails!")
        print("Computer will start.")
        if comp_choice == 1 :
            row_one[0] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 2 :
            row_one[1] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 3 :
            row_one[2] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 4 :
            row_two[0] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 5 :
            row_two[1] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 6 :
            row_two[2] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 7 :
            row_three[0] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 8 :
            row_three[1] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        else:
            row_three[2] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
    elif order == "T" and coin_flip == 1:
        if coin_flip == 1:
            print("It's heads!")
        else:
            print("It's tails!")
        print("Computer will start.")
        if comp_choice == 1 :
            row_one[0] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 2 :
            row_one[1] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 3 :
            row_one[2] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 4 :
            row_two[0] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 5 :
            row_two[1] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 6 :
            row_two[2] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 7 :
            row_three[0] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        elif comp_choice == 8 :
            row_three[1] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
        else:
            row_three[2] = "O"
            print(f"{row_one} \n{row_two} \n{row_three}")
    else:
        print("Not an option, bud.")
        break
