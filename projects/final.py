# GNB - 1st - Final Project

#IMPORT RANDOM LIBRARY
import random

#WELCOME USER TO “FREE GAME BASED IN THE HOOD”
print("Welcome, User, to a Free Game Based in the Hood!")

#EXPLAIN:
print("In this game, you'll experience life as you have relationships (best friend, significant other, etc.), know what it's kind of like to be part of a gang, and fight your big bro in a final battle of shadow boxing.\nYou'll be living a week in the life; everyday you'll have the option to go at most three different places (or even just stay at the same place) and do some things there.\nYou can live out the entire week, if you don't die...death = GAME OVER!")

# - PLAYER MUST BALANCE GANG LIFE, SIGNIFICANT OTHER, BEST FRIEND, AND JOB
# - EVERY ACTION TAKES 1/3 OF A DAY
# - GAME LASTS 7 DAYS IF THEY DO NOT DIE
# - FINAL BOSS BATTLE USES SHADOW BOXING/ISH MECHANICS


#DECLARE SMARTS = RANDOM NUMBER (0–215)
smarts_stat = random.randint(0, 215)

#DECLARE STREET_RESPECT = RANDOM NUMBER (0–300)
street_respect_stat = random.randint(0, 300)

#DECLARE STEALTH = 0
stealth_stat = 10

#DECLARE MONEY = RANDOM NUMBER (1,000)
money_stat = 1000

#DECLARE FIGHT_DAMAGE = RANDOM NUMBER (5–8)
fight_damage_stat = random.randint(5, 8)

#DECLARE PLAYER_HEALTH = 100  # Player's health starts at 100
health_stat = 100

# USER STATS
print(f"Now you'll get your randomly generated stats:\nSmarts/IQ: {smarts_stat}\nStreet Respect: {street_respect_stat}\nStealth: {stealth_stat}\nMoney: {money_stat}\nFight Damage: {fight_damage_stat}\nHealth: {health_stat}\n")




# ITEM SYSTEM

#DECLARE INVENTORY = STARTING ITEMS
inventory = ["Fists/5DMG"]

#DECLARE ITEM_1 = “BASIC WEAPON”
item_knife = "Small Knife"

#DECLARE ITEM_2 = “STEALTH HOODIE”
item_stealth_hood = "Stealthy Hoodie"

#DECLARE ITEM_WEAPON_PICKED = FALSE
item_knife_picked = False

#DECLARE ITEM_HOODIE_PICKED = FALSE
item_stealth_hood_picked = False


# SUPPORTING FUNCTIONS

#DEFINE FUNCTION MODIFY_STATS(stat_name, amount):
#     CHANGE THE SPECIFIED PLAYER STAT BY THE GIVEN AMOUNT
def modify_stats(stat_name, amount):
    global smarts_stat, street_respect_stat, stealth_stat, money_stat, fight_damage_stat, health_stat
    if stat_name == "smarts":
        smarts_stat += amount
    elif stat_name == "street_respect":
        street_respect_stat += amount
    elif stat_name == "stealth":
        stealth_stat += amount
    elif stat_name == "money":
        money_stat += amount
    elif stat_name == "fight_damage":
        fight_damage_stat += amount
    elif stat_name == "health":
        health_stat += amount


#DEFINE FUNCTION PICKUP_ITEM(item):
#     IF item HAS NOT ALREADY BEEN PICKED UP:
#          ADD item TO INVENTORY
#          APPLY THE RELEVANT STAT BOOST TO PLAYER
#          MARK item AS PICKED UP
def pickup_item(item_picked_flag_name, item, stat_name=None, amount=0):
    global item_knife_picked, item_stealth_hood_picked

    # Check if the item has already been picked up
    if not globals()[item_picked_flag_name]:
        inventory.append(item)
        globals()[item_picked_flag_name] = True
        if stat_name is not None:
            modify_stats(stat_name, amount)
        print(f"You picked up {item}!")
    else:
        print(f"You already have the {item}.")


#DEFINE FUNCTION COMBAT_SYSTEM(enemy_name, enemy_health, enemy_damage):
#     LOOP WHILE BOTH PLAYER_HEALTH AND enemy_health ARE GREATER THAN 0:
#          DISPLAY PLAYER OPTIONS: ATTACK, DODGE, USE ITEM
#          GET PLAYER CHOICE
#          CALCULATE DAMAGE TO enemy_health AND PLAYER_HEALTH BASED ON CHOICE AND STATS
#          IF enemy_health IS LESS THAN OR EQUAL TO 0:
#               BREAK LOOP AND INCREASE STREET_RESPECT
#          IF PLAYER_HEALTH IS LESS THAN OR EQUAL TO 0:
#               DISPLAY GAME OVER AND END GAME
#     ENSURE ENEMY DOES NOT RESPAWN AFTER DEFEAT        
def combat(enemy_name, enemy_health, enemy_damage, health_stat, user_fight_choice):
    #enemy_damage = random.randint(5, 20)
    #enemy_health = random.randint(45, 175)

    turn = random.choice(["user", "enemy"])
    
    enemy_fight_choice = random.choice(["attack", "dodge"])
    
    print(f"Oh no! You're getting jumped by {enemy_name}!")
    while enemy_health > 0 and health_stat > 0:
        if turn == "user":
            user_fight_choice = input("What do you want to do?: attack? - dodge? - run away? (type the word/words in letter for letter)").strip().lower()
            if user_fight_choice == "attack":
                attack_weapon_choice = input(f"Which weapon do you want to use from your? (type the word/words in letter for letter): {inventory}").strip()

                if attack_weapon_choice == "Fists":
                    enemy_health = enemy_health - 5
                    print(enemy_health)

            elif user_fight_choice == "dodge":
                user_dodge_success = random.randint(1, 5) #TWENTY PERCENT CHANCE DODGE FAILS
            elif user_fight_choice == "run away":
                user_escape_chance = random.randint(1, 10) #TEN PERCENT CHANCE ESCAPE FAILS
                if user_escape_chance == 6:
                    print(f"{enemy_name} snatched you before you could escape, and hit you!")
                    health_stat = health_stat - enemy_damage
                else:
                    print("Imagine running from a fight like a scaredy cat. 💔")
                    street_respect_stat = street_respect_stat - 15
            else:
                print("You tried to dodge but got hit!")

        elif user_fight_choice == "run away":
            escape_chance = random.randint(1, 10)
            if escape_chance > 7:
                print("You escaped successfully!")
                return
            else:
                print(f"{enemy_name} caught you and hit you!")
                health_stat -= enemy_damage
        else:
            if enemy_fight_choice == "attack" and user_fight_choice == "dodge":
                def dodge():
                    if user_dodge_success == 1:
                        print("Imagine trying to dodge, and still getting hit. 💀")
                        health_stat = health_stat - enemy_damage
                    else:
                        print("You dodged successfully!")
                        #continue
                    dodge()
            elif enemy_fight_choice == "attack" and user_fight_choice == "attack":
                health_stat = health_stat - enemy_damage
              #  enemy_health = enemy_health - weapon_damage
            elif enemy_fight_choice == "dodge" and user_fight_choice == "attack":
                    enemy_dodge_success = random.randint(1, 5) #TWENTY PERCENT CHANCE DODGE FAILS
                    if user_dodge_success == 1:
                        print(f"{enemy_name} tried to dodge your attack, but you still hit them!")
                #        enemy_health = enemy_health - weapon_damage
                    else:
                        print(f"{enemy_name} dodged your attack successfully!")
                        continue

        if health_stat <= 0:
            print("You died - Game Over!!!")
            exit()



#print(combat("Jordan", random.randint(45, 175), random.randint(5, 20), 100, input()))

# BOSS BATTLE SYSTEM SETUP

#DISPLAY INSTRUCTIONS:
# - SHADOW BOXING RULES:
#   * POINTER CHOOSES A DIRECTION TO POINT (UP, DOWN, LEFT, RIGHT)
#   * LOOKER MUST FOLLOW BY LOOKING IN THAT DIRECTION
#   * POINTER NEEDS TO GET THE LOOKER TO LOOK IN 3 DIFFERENT DIRECTIONS IN A ROW, EACH CORRECT FOLLOWING POINTER’S DIRECTION
#   * AFTER EACH SUCCESSFUL MATCH, THAT DIRECTION IS REMOVED FROM FUTURE POINTER CHOICES
#   * IF THE LOOKER LOOKS AWAY FROM THE POINTED DIRECTION, ROLES SWITCH (LOOKER BECOMES POINTER AND VICE VERSA)
#   * THE FIRST TO GET 3 SUCCESSFUL CONSECUTIVE DIRECTION MATCHES WINS


#DECLARE USER_ISH_DIRECTIONS = ["UP","DOWN","LEFT","RIGHT"]
user_ish_directions = ["UP", "DOWN", "LEFT", "RIGHT"]

#DECLARE COMP_ISH_DIRECTIONS = ["UP","DOWN","LEFT","RIGHT"]
comp_ish_directions = ["UP", "DOWN", "LEFT", "RIGHT"]


#DECLARE USER_ISH_CHOICE = USER INPUT (SELECT DIRECTION FROM ALLOWED OPTIONS)
#DECLARE COMP_ISH_CHOICE = RANDOMLY SELECTED FROM COMP_ISH_DIRECTIONS


#DECLARE COINFLIP:
# USER CHOOSES HEADS OR TAILS
# RANDOM RESULT DECIDES WHO GOES FIRST
def coinflip():
    user_call = input("Heads or tails? ").strip().lower()
    flip_result = random.choice(["heads", "tails"])
    print(f"The coin landed on {flip_result}.")
    return user_call == flip_result


# DICTIONARIES FOR CHARACTERS

#DECLARE CHARACTERS DICTIONARY:
characters = {
    "BEST FRIEND": "LEBRONITO",
    "SIGNIFICANT OTHER": "PO",
    "GANG LEADER": "REGINALD",
    "BIG BROTHER": "JEREMIAH",
    "OPP GANG LEADER": "JUJU-LAWRENCE",
    "HOMELESS MAN": "JARVIS",
    "HOMELESS WOMAN": "CECE"
}


# LOCATIONS LIST

#DECLARE LOCATIONS:
locations = [
    "HOME",
    "BESTIE_HOME",
    "SIGNIFICANT_OTHER_HOME",
    "GANG_SPOT",
    "MCDONALDS",
    "GAS_STATION",
    "ALLEYWAY",
    "OUTSIDE",
    "HOSPITAL",
    "OPPS_TERRITORY"
]


# ITEMS WITH DAMAGE (ONLY CAN BE FOUND IN RANDOM PLACES) LIST

items_with_damage = {
    "MACHETE": 10,
    "PISTOL": 16,
    "PEPPER SPRAY": 4,
    "BRASS KNUCKLES": random.randint(7, 13),
    "GRENADE": 67
}

# ITEMS WITH DAMAGE (ONLY CAN BE BOUGHT OFF AMAZON) LIST

amazon_weapons = {
    "KATANA": {"damage": 17, "price": 30},
    "DRACO": {"damage": 20, "price": 50},
    "WOLVERINE CLAWS": {"damage": 15, "price": 42},
    "ROCKET LAUNCHER": {"damage": 75, "price": 567},
    "FLASHBANG": {"damage": 20, "price": 67}
}


# ACTIONS LIST

actions = [
    "HANG AROUND",
    "GOOF OFF",
    "TALK TRASH TO OPPS ON LIVE",
    "ROB SOMEONE/PLACE",
    "EAT/BUY SOMETHING",
    "HIDE THERE"
]



#DEFINE FUNCTION ORDER_WEAPON_FROM_AMAZON():
def order_weapon_from_amazon():
    global money_stat, fight_damage_stat

    print("\n--- AMAZON WEAPON SHOP ---")
    for weapon in amazon_weapons:
        print(f"{weapon} | Damage: {amazon_weapons[weapon]['damage']} | Price: ${amazon_weapons[weapon]['price']}")

    choice = input("Type the name of the weapon you want to buy (or 'leave'): ")

    if choice in amazon_weapons:
        price = amazon_weapons[choice]["price"]
        damage = amazon_weapons[choice]["damage"]

        if money_stat >= price:
            money_stat -= price
            inventory.append(f"{choice}/{damage}DMG")
            fight_damage_stat = damage
            print(f"You bought the {choice}. Damage set to {damage}.")
        else:
            print("You don't have enough money.")

    else:
        print("You left Amazon website.")

# TALK TRASH ON LIVE FUNCTION (USED IN ALL LOCATIONS)
def talk_trash_on_live():
    global street_respect_stat, health_stat
    print("\nYou go live and start talking crazy to the opps...")
    outcome = random.randint(1, 5)

    if outcome >= 3:
        street_respect_stat += 10
        print("Your live went viral. Street respect +10.")
    else:
        health_stat -= 5
        print("Opps saw the live and pressed you later. Health -5.")



# LOCATION FUNCTIONS

def LOCATION_SELECTOR():
    print("\nWhere do you want to go?")
    for loc in locations:
        print("-", loc)

    choice = input("Type location name: ").upper()

    if choice == "HOME":
        home()
        actions += 1
    elif choice == "BESTIE_HOME":
        bestie_home()
        actions += 1
    elif choice == "SIGNIFICANT_OTHER_HOME":
        significant_other_home()
        actions += 1
    elif choice == "GANG_SPOT":
        gang_spot()
        actions += 1
    elif choice == "MCDONALDS":
        work_mcdonalds()
        actions += 1
    elif choice == "GAS_STATION":
        gas_station()
        actions += 1
    elif choice == "ALLEYWAY":
        alleyway()
        actions += 1
    elif choice == "OUTSIDE":
        outside()
        actions += 1
    elif choice == "HOSPITAL":
        hospital()
        actions += 1
    elif choice == "OPPS_TERRITORY":
        opps_territory()
        actions += 1
    else:
        print("Invalid location.")

#DEFINE FUNCTION HOME():
def home():
    global smarts_stat, street_respect_stat, money_stat

    print("\nYou are at HOME.")
    print("Options: sleep, eat, play games, invite best friend, invite significant other, read, order weapon, go somewhere else, talk trash, hide")

    choice = input("Choose an action: ").strip().lower()

    if choice == "read":
        modify_stats("smarts", 10)
        print("You read and increased your smarts!")

    elif choice == "order weapon":
        order_weapon_from_amazon()
        actions += 1

    elif choice == "talk trash":
        talk_trash_on_live()
        actions += 1

    elif choice == "go somewhere else":
        LOCATION_SELECTOR()

    elif choice == "sleep":
        print("You rest and regain some health.")
        modify_stats("health", 10)
        actions += 1

    elif choice == "eat":
        if money_stat >= 10:
            money_stat -= 10
            print("You ate food and feel better.")
            modify_stats("health", 5)
        else:
            print("Not enough money to eat.")

    elif choice == "play games":
        print("You played games and relaxed.")

    elif choice == "invite best friend":
        print(f"You invited your best friend {characters['BEST FRIEND']} over.")
        actions += 1

    elif choice == "invite significant other":
        print(f"You invited your significant other {characters['SIGNIFICANT OTHER']} over.")
        actions += 1

    elif choice == "hide":
        print("You hide for a while.")

    else:
        print("Action not recognized.")


#DEFINE FUNCTION BESTIE_HOME():
def bestie_home():
    global smarts_stat

    print("\nYou are at your BESTIE'S HOME.")
    print("Options: sleep, eat, hang out, read, order weapon, go somewhere else, talk trash")

    choice = input("Choose an action: ").strip().lower()

    if choice == "read":
        modify_stats("smarts", 7)
        print("You read and increased your smarts!")

    elif choice == "order weapon":
        order_weapon_from_amazon()
        actions += 1

    elif choice == "talk trash":
        talk_trash_on_live()
        actions += 1

    elif choice == "hang out":
        print(f"You hang out with your best friend {characters['BEST FRIEND']}.")
        actions += 1

    elif choice == "go somewhere else":
        LOCATION_SELECTOR()

    elif choice == "sleep":
        print("You sleep and regain some health.")
        modify_stats("health", 10)
        actions += 1

    elif choice == "eat":
        print("You ate some food.")

    else:
        print("Action not recognized.")


#DEFINE FUNCTION SIGNIFICANT_OTHER_HOME():
def significant_other_home():
    global smarts_stat

    print("\nYou are at your SIGNIFICANT OTHER'S HOME.")
    print("Options: sleep, eat, hang out, read, order weapon, go somewhere else, talk trash, hide")

    choice = input("Choose an action: ").strip().lower()

    if choice == "read":
        modify_stats("smarts", 7)
        print("You read and increased your smarts!")

    elif choice == "order weapon":
        order_weapon_from_amazon()
        actions += 1

    elif choice == "talk trash":
        talk_trash_on_live()
        actions += 1

    elif choice == "hang out":
        print(f"You hang out with your significant other {characters['SIGNIFICANT OTHER']}.")
        actions += 1

    elif choice == "go somewhere else":
        LOCATION_SELECTOR()

    elif choice == "sleep":
        print("You sleep and regain some health.")
        modify_stats("health", 10)
        actions += 1

    elif choice == "eat":
        print("You ate some food.")

    elif choice == "hide":
        print("You hide at your significant other's place.")

    else:
        print("Action not recognized.")


#DEFINE FUNCTION GANG_SPOT():
def gang_spot():
    global smarts_stat

    print("\nYou are at the GANG SPOT.")
    print("Options: hang out, read, order weapon, go somewhere else, talk trash, hide")

    choice = input("Choose an action: ").strip().lower()

    if choice == "hang out":
        print(f"You hang out with your gang.")
        actions += 1

    elif choice == "read":
        modify_stats("smarts", 7)
        print("You read and increased your smarts!")

    elif choice == "order weapon":
        order_weapon_from_amazon()
        actions += 1

    elif choice == "talk trash":
        talk_trash_on_live()
        actions += 1

    elif choice == "go somewhere else":
        LOCATION_SELECTOR()

    elif choice == "hide":
        print("You hide at the gang spot.")

    else:
        print("Action not recognized.")


#DEFINE FUNCTION WORK_MCDONALDS():
def work_mcdonalds():
    global money_stat, street_respect_stat

    print("\nYou are at McDonald's work.")
    print("Options: work, skip work")

    choice = input("Choose an action: ").strip().lower()

    if choice == "work":
        earned = random.randint(50, 150)
        money_stat += earned
        print(f"You worked and earned ${earned}.")
        actions += 1

    elif choice == "skip work":
        street_respect_stat -= 20
        print("You skipped work. Street respect dropped.")
        LOCATION_SELECTOR()

    else:
        print("Action not recognized.")


#DEFINE FUNCTION GAS_STATION():
def gas_station():
    global money_stat, street_respect_stat

    print("\nYou are at the GAS STATION.")
    print("Options: buy food, rob, talk trash")

    choice = input("Choose an action: ").strip().lower()

    if choice == "buy food":
        if money_stat >= 5:
            money_stat -= 5
            print("You bought food.")
        else:
            print("Not enough money.")

    elif choice == "rob":
        chance = random.randint(1, 10)
        actions += 1
        if chance == 3:
            money_stat -= 20
            street_respect_stat -= 15
            print("Caught robbing! Lost money, respect, and health.")
        elif chance == 5:
            money_stat -= 20
            street_respect_stat -= 15
            print("Caught robbing! Lost money, respect, and health.")
        elif chance == 4:
            money_stat -= 20
            street_respect_stat -= 15
            print("Caught robbing! Lost money, respect, and health.")
        elif chance == 6:
            print("The cashier had a gun, and shot you in the head!")
            print("You died - Game Over!!!")
            exit()
        else:
            gained = random.randint(20, 150)
            money_stat += gained
            print(f"Robbery successful! You got ${gained}.")

    elif choice == "talk trash":
        talk_trash_on_live()
        actions += 1

    else:
        print("Action not recognized.")


#DEFINE FUNCTION ALLEYWAY():
def alleyway():
    global money_stat, street_respect_stat, health_stat, smarts_stat, stealth_stat

    print("\nYou are in the ALLEYWAY.")
    print("Options: proceed, hide, do illegal things, rob, talk trash")

    choice = input("Choose an action: ").strip().lower()

    if choice == "proceed":
        encounter = random.choice([True, False])
        actions += 1
        if encounter:
            print("You encountered an enemy!")
            combat("Alley Opp", random.randint(30, 60), random.randint(5, 15))
        else:
            print("No enemies here.")

    elif choice == "hide":
        print("You hide successfully.")

    elif choice == "do illegal things":
        chance = random.randint(1, 10)
        actions += 1
        if chance > (smarts_stat // 30) + (stealth_stat // 10):
            print("You did illegal things without getting caught.")
        else:
            money_stat -= 30
            street_respect_stat -= 20
            print("Caught! Lost money and respect.")
    elif choice == "rob":
        chance = random.randint(1, 10)
        actions += 1
        if chance == 6:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        elif chance == 7:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        elif chance == 8:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        else:
            money_stat += random.randint(0, 900)
            street_respect_stat += 20
            print(f"You robbed them successfully, and now have ${money_stat}, and {street_respect_stat} street respect!")

#DEFINE FUNCTION OUTSIDE():
def outside():
    global money_stat, street_respect_stat, health_stat, smarts_stat, stealth_stat

    print("\nYou are OUTSIDE.")
    print("Options: proceed, do illegal things, rob, talk trash")

    choice = input("Choose an action: ").strip().lower()

    if choice == "proceed":
        encounter = random.choice([True, False])
        actions += 1
        if encounter:
            print("You encountered an enemy!")
            combat(random.choice["Homeless Crackhead named Jarvis", "Homeless Crackhead named Gigi"], random.randint(30, 60), random.randint(5, 15))
        else:
            print("No enemies here.")


    elif choice == "do illegal things":
        chance = random.randint(1, 10)
        actions += 1
        if chance > (smarts_stat // 30) + (stealth_stat // 10):
            print("You did illegal things without getting caught.")
        else:
            money_stat -= 30
            street_respect_stat -= 20
            print("Caught! Lost money and respect.")
    elif choice == "rob":
        chance = random.randint(1, 10)
        actions += 1
        if chance == 6:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        elif chance == 7:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        elif chance == 8:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        else:
            money_stat += random.randint(0, 900)
            street_respect_stat += 20
            print(f"You robbed them successfully, and now have ${money_stat}, and {street_respect_stat} street respect!")

def hospital():
    global money_stat, health_stat
    if money_stat >= 100:
        print("You don't have enough money to heal yourself up fully.")
    else:
        money_stat -= 100
        health_stat = 100
        print("You got fully healed")
#DEFINE FUNCTION ALLEYWAY():
def opps_territory():
    global money_stat, street_respect_stat, health_stat, smarts_stat, stealth_stat

    print("\nYou are deep in the opps territory.")
    print("Options: proceed, rob, talk trash")

    choice = input("Choose an action: ").strip().lower()

    if choice == "proceed":
        encounter = random.choice([True, False])
        actions += 1
        if encounter:
            print("You encountered an opp!")
            combat("Opp Gang member", random.randint(30, 60), random.randint(5, 15))
        else:
            print("No enemies here.")

    elif choice == "do illegal things":
        chance = random.randint(1, 10)
        actions += 1
        if chance > (smarts_stat // 30) + (stealth_stat // 10):
            print("You did illegal things without getting caught.")
        else:
            money_stat -= 30
            street_respect_stat -= 20
            print("Caught! Lost money and respect.")
    elif choice == "rob":
        chance = random.randint(1, 10)
        actions += 1
        if chance == 6:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        elif chance == 7:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        elif chance == 8:
            print("They aren't giving up without a fight!")
            combat(random.choice["Janice", "Aaron", "LeBron", "Oprah Winfrey"], random.randint(50, 100), random.randint(2, 25))
        else:
            money_stat += random.randint(0, 900)
            street_respect_stat += 20
            print(f"You robbed them successfully, and now have ${money_stat}, and {street_respect_stat} street respect!")
    elif choice == "talk trash":
        print("Why would you talk trash on live in opp-town?")
        combat(random.choice["Jeremy", "DaQuavion", "Josh", "Dillon", "Von III"], random.randint(45, 135), random.randint(10, 30))
        

# TIME/DAY LOOP

#DECLARE DAY = 1

day = 1
actions = 0
#WHILE DAY IS LESS THAN OR EQUAL TO 7:
#     DISPLAY CURRENT DAY NUMBER
#     CALL HOME FUNCTION TO ALLOW PLAYER ACTIONS
#     AFTER PLAYER COMPLETES 3 ACTIONS:
#          INCREMENT DAY BY 1

while day <= 7:
    print(f"IT'S DAY {day}")
    if actions == 3:
        day += 1


# FINAL BOSS FIGHT

#WHEN DAY REACHES 7:
#     DISPLAY MESSAGE THAT FINAL FIGHT IS BEGINNING
#     CALL FINAL_BOSS_BATTLE FUNCTION

#DEFINE FUNCTION FINAL_BOSS_BATTLE():
#     DISPLAY SHADOW BOXING RULES TO PLAYER
#     SET pointer = PLAYER
#     SET looker = BOSS
#     SET streak = 0
#     SET allowed_directions = ["UP", "DOWN", "LEFT", "RIGHT"]

#     LOOP INDEFINITELY:
#          pointer_choice = GET INPUT FROM pointer (choose direction from allowed_directions)
#          looker_choice = GET INPUT FROM looker (random choice if computer)

#          IF pointer_choice EQUALS looker_choice:
#               INCREASE streak BY 1
#               REMOVE pointer_choice FROM allowed_directions
#               DISPLAY "Match! Current streak: " + streak

#               IF streak EQUALS 3:
#                    DISPLAY "Pointer wins the shadow boxing!"
#                    BREAK LOOP

#          ELSE:
#               DISPLAY "Looker in a different direction! Roles switch!"
#               SWAP pointer AND looker
#               RESET streak TO 0
#               RESET allowed_directions TO ["UP", "DOWN", "LEFT", "RIGHT"]

#     IF PLAYER IS pointer (i.e. player won):
#          DISPLAY VICTORY MESSAGE

#     ELSE:
#          DISPLAY GAME OVER MESSAGE


# END OF GAME

#IF PLAYER SURVIVES ALL 7 DAYS AND DEFEATS BOSS:
#     DISPLAY ENDING AND CREDITS

#IF PLAYER_HEALTH IS LESS THAN OR EQUAL TO 0 AT ANY TIME:
#     DISPLAY GAME OVER MESSAGE