# GNB - 1st - 🔨 Combat Program
import random

order = random.randint(1,2)

class_choice = input("Welcome to an interesting game...What class of fighter do you want to be? \n1 for a dude with a 67 inch, sharp blade; and some other cool stuff \n2 for a dude that knows some pretty powerful magic, and some other interesting possesions \n3 for a dude with aura that just kills, who also has some pretty cool things\n")

if class_choice == "1":
    print("Great choice - Here are your stats:\nHealth: 30 \nDefense: 15 \nAttack: 17-40 \nDamage: 8-11")
elif class_choice == "2":
    print("Cool choice - Here are your stats:\nHealth: 40 \nDefense: 19 \nAttack: 15-30 \nDamage: 6-9")
elif class_choice == "3":
    print("That's such a tuff choice - Here are your stats:\nHealth: 50 \nDefense: 20 \nAttack: 1-60 \nDamage: 10-30 \nAura: ∞")
else:
    print("YOU DUM-DUM, THAT'S NOT AN OPTION - anyway, leave please.")





















































