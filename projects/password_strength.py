# GNB - 1st - 💡Password Strength Checker

#Create variable for points, which should be starting at zero
points = 0
#Use input to ask for User's password
password = input("Enter a password (at least 8 characters long), and on a scale of 1-5 I'll tell you how strong it is:\n")
#Place everything in a while loop (while True)
while True:
    #Include if statement to check for password length - make variable for password length - add point if password is long enough - display whether or not password is long enough and whether or not length met requirement
    password_length = len(password)
    if password_length < 8:
        print("8+ characters: ❌")
        points += 0
    else:
        print("8+ characters: ✅")
        points += 1

    #Use if statements to check password input for uppercase, lowercase, numbers, and special characters

    #Uppercase - check for every uppercase letter in the English language, if at least one is there, then add one point - display whether or not there's uppercase letters
    if any(char.isupper() for char in password):
        points += 1
        print("Contains Uppercase letters: ✅")
    else:
        points += 0
        print("Contains Uppercase letters: ❌")


    #Lowercase - check for every lowercase letter in the English language, if at least one is there, then add one point - display whether or not there's lowercase letters
    if any(char.islower() for char in password):
        points += 1
        print("Contains Lowercase letters: ✅") 
    else:
        points += 0
        print("Contains Lowercase letters: ❌")
    #Numbers - check for every number on the keyboard, if there's at least one, add a point - display whether or not there's numbers
    if any(char.isdigit() for char in password):
        points += 1
        print("Contains Numbers: ✅")
    else:
        points += 0
        print("Contains Numbers: ❌")
    #Special Characters - check for every special character on the keyboard, if at least one is there, then add one point - display whether or not there's special characters - mention variable special_chars as all special chars
    special_chars = "!@#$%^&*()_+-=[]}{|;:,.<>?~`/\\"
    if any(char in special_chars for char in password):
        points += 1
        print("Contains Special characters: ✅")
    else:
        points += 0
        print("Contains Special characters: ❌")
    
    if points <= 2:
        print(f"Password is weak - {points}/5 points")
    elif points == 3:
        print(f"Password is moderate - {points}/5 points")    
    elif points == 4:
        print(f"Password is weak - {points}/5 points")
    else:
        print(f"Password is very strong - {points}/5 points")
    break