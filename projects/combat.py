# GNB - 1st - 🔨 Combat Program
import random

order = random.randint(1,2)

monster_health = random.randint(20,75)
monster_defense = random.randint(5,30)

class_choice = input("Welcome to an interesting game...What class of fighter do you want to be? \n1 for a dude with a 67 inch, sharp blade; and some other cool stuff \n2 for a dude that knows some pretty powerful magic, and some other interesting possesions \n3 for a dude with aura that just kills, who also has some pretty cool things\n").strip()

if class_choice == "1":
    print("Great choice - Here are your stats:\nHealth: 30 \nDefense: 15 \nAttack: 1-40 \nDamage: 8-11")
elif class_choice == "2":
    print("Cool choice - Here are your stats:\nHealth: 40 \nDefense: 19 \nAttack: 1-30 \nDamage: 6-9")
elif class_choice == "3":
    print("That's such a tuff choice - Here are your stats:\nHealth: 50 \nDefense: 20 \nAttack: 1-60 \nDamage: 10-30 \nAura: ∞")
else:
    print("YOU DUM-DUM, THAT'S NOT AN OPTION - anyway, leave please.")

print(f"A monster! \nIt has {monster_health} health :O")
if order == 1:
    def bladeDude(blade_attack):
        blade_attack = random.randint(17,41)
        blade_damage = random.randint(8,12)
        if blade_attack >= monster_defense:
            monster_health = monster_health - blade_damage

    print(f"Now it's got {monster_health}")








































