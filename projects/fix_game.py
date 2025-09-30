# GNB - 1st - 🔨 Fix the Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0 #Also mention attempts variable before saying that you'll add on to it
    game_over = False
    while not game_over:
        attempts += 1 
    #Never made it so that the amount of attempts used could go up - would've allowed user to guess forever without hitting the max attempts - logic
        guess = int(input("Enter your guess: \n")) 
    #Didn't make the input an integer - runtime - it wasn't able to accept answers that weren't strings, (it would crash) but the answers had to be integers
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        if attempts >= max_attempts: 
        #Shouldn't be checking if it used an attempt before checking if the guess is (in)correct (if it were last attempt used, the code would say that the user had run out of guesses before saying it was correct, and it'd be all messed up) - logic
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        else: pass
    #Remove the "continue" thing - it does nothing for the code, and when the game is eventually over, it causes the code to skip over the game over... sentence - logic
    print("Game Over. Thanks for playing!")
start_game()