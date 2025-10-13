# GNB - 1st - 💡Password Strength Checker

#Create variable for points, which should be starting at zero
points = 0
#Use input to ask for User's password
password = input("Enter a password (at least 8 characters long), and on a scale of 1-5 I'll tell you how strong it is:\n").strip()
#Include if statement to check for password length - make variable for password length - add point if password is long enough
password_length = len(password)
if password_length < 8:
    print("Password isn't long enough.")
else:
    print("8+ characters: ✅")
    points += 1

#Use if statements to check password input for uppercase, lowercase, numbers, and special characters

#Uppercase - check for every uppercase letter in the English language, if at least one is there, then add one point
if "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" in password:
    points += 1
    print("Contains Uppercase letters: ✅")
else:
    points += 0

#Lowercase - check for every lowercase letter in the English language, if at least one is there, then add one point
if "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" in password:
    points += 1
    print("Contains Lowercase letters: ✅")
else:
    points += 0
#Numbers - check for every number on the keyboard, if there's at least one, add a point
if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in password:
    points += 1
    print("Contains Numbers: ✅")
else:
    points += 0
#Special Characters - check for every special character on the keyboard, if at least one is there, then add one point
if "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "`" or "~" or "-" or "_" or "=" or "+" or "[" or "]" or "{" or "}" or "\\" or "|" or "," or "<" or "." or ">" or "/" or "?" in password:
    print("Contains Special characters: ✅")
    points += 1
else:
    points += 0

#✅ ❌