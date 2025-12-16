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
    "BESTIE HOME",
    "SIGNIFICANT OTHER HOME",
    "GANG SPOT",
    "MCDONALDS",
    "GAS STATION",
    "ALLEYWAY",
    "OUTSIDE",
    "HOSPITAL",
    "OPPS TERRITORY"
]

# ITEMS WITH DAMAGE (ONLY CAN BE BOUGHT OFF AMAZON) LIST

amazon_weapons = {
    "KATANA": {"damage": 17, "price": 30},
    "DRACO": {"damage": 20, "price": 50},
    "WOLVERINE CLAWS": {"damage": 15, "price": 42},
    "ROCKET LAUNCHER": {"damage": 75, "price": 567},
    "FLASHBANG": {"damage": 20, "price": 67},
    "MACHETE": {"damage": 15, "price": 25},
    "PISTOL": {"damage": 19, "price": 36},
    "PEPPER SPRAY": {"damage": 6, "price": 15},
    "BRASS KNUCKLES": {"damage": random.randint(7, 13), "price": 18} ,
    "GRENADE": {"damage": 60, "price": 67}
}


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


#DEFINE FUNCTION ORDER_WEAPON_FROM_AMAZON():
def order_weapon_from_amazon():
    global money_stat, fight_damage_stat

    print("\n--- AMAZON WEAPON SHOP ---")
    for weapon in amazon_weapons:
        print(f"{weapon} | Damage: {amazon_weapons[weapon]['damage']} | Price: ${amazon_weapons[weapon]['price']}")

    choice = input("Type the name of the weapon you want to buy (or 'leave'): ").strip().upper()

    if choice in amazon_weapons:
        price = amazon_weapons[choice]["price"]
        damage = amazon_weapons[choice]["damage"]

        if money_stat >= price:
            money_stat -= price
            inventory.append(f"{choice}/{'damage'}DMG")
            print(f"You bought the {choice} for {price} dollars. And it does {damage} damage.")
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

def location_selector():
    print("\nWhere do you want to go?")
    for loc in locations:
        print("-", loc)

    choice = input("Type location name: ").strip().upper()

    if choice == "HOME":
        home()
    elif choice == "BESTIE HOME":
        bestie_home()
    elif choice == "SIGNIFICANT OTHER HOME":
        significant_other_home()
    elif choice == "GANG SPOT":
        gang_spot()
    elif choice == "MCDONALDS":
        work_mcdonalds()
    elif choice == "GAS STATION":
        gas_station()
    elif choice == "ALLEYWAY":
        alleyway()
    elif choice == "OUTSIDE":
        outside()
    elif choice == "HOSPITAL":
        hospital()
    elif choice == "OPPS TERRITORY":
        opps_territory()
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

    elif choice == "talk trash":
        talk_trash_on_live()

    elif choice == "go somewhere else":
        location_selector()

    elif choice == "sleep":
        print("You rest and regain some health.")
        modify_stats("health", 10)

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

    elif choice == "invite significant other":
        print(f"You invited your significant other {characters['SIGNIFICANT OTHER']} over.")

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

    elif choice == "talk trash":
        talk_trash_on_live()

    elif choice == "hang out":
        print(f"You hang out with your best friend {characters['BEST FRIEND']}.")

    elif choice == "go somewhere else":
        location_selector()

    elif choice == "sleep":
        print("You sleep and regain some health.")
        modify_stats("health", 10)

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

    elif choice == "talk trash":
        talk_trash_on_live()

    elif choice == "hang out":
        print(f"You hang out with your significant other {characters['SIGNIFICANT OTHER']}.")

    elif choice == "go somewhere else":
        location_selector()

    elif choice == "sleep":
        print("You sleep and regain some health.")
        modify_stats("health", 10)

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

    elif choice == "read":
        modify_stats("smarts", 7)
        print("You read and increased your smarts!")

    elif choice == "order weapon":
        order_weapon_from_amazon()

    elif choice == "talk trash":
        talk_trash_on_live()

    elif choice == "go somewhere else":
        location_selector()

    elif choice == "hide":
        print("You hide at the gang spot.")

    else:
        print("Action not recognized.")


#DEFINE FUNCTION WORK_MCDONALDS():
def work_mcdonalds():
    global money_stat, street_respect_stat

    print("\nYou are at McDonald's work.")
    print("Options: work, skip work, go somewhere else")

    choice = input("Choose an action: ").strip().lower()

    if choice == "work":
        earned = random.randint(50, 150)
        money_stat += earned
        print(f"You worked and earned ${earned}.")

    elif choice == "skip work":
        street_respect_stat -= 20
        print("You skipped work. Street respect dropped.")

    elif choice == "go somewhere else":
        location_selector()

    else:
        print("Action not recognized.")


#DEFINE FUNCTION GAS_STATION():
def gas_station():
    global money_stat, street_respect_stat

    print("\nYou are at the GAS STATION.")
    print("Options: buy food, rob, talk trash, go somewhere else")

    choice = input("Choose an action: ").strip().lower()

    if choice == "buy food":
        if money_stat >= 5:
            money_stat -= 5
            print("You bought food.")
        else:
            print("Not enough money.")

    elif choice == "rob":
        chance = random.randint(1, 10)
        if chance <= 3:
            money_stat -= 20
            street_respect_stat -= 15
            print("Caught robbing! Lost money and respect.")
        else:
            gained = random.randint(20, 50)
            money_stat += gained
            print(f"Robbery successful! You got ${gained}.")

    elif choice == "talk trash":
        talk_trash_on_live()
        
    elif choice == "go somewhere else":
        location_selector()

    else:
        print("Action not recognized.")


#DEFINE FUNCTION ALLEYWAY():
def alleyway():
    global money_stat, street_respect_stat, health_stat, smarts_stat, stealth_stat

    print("\nYou are in the ALLEYWAY.")
    print("Options: proceed, hide, do illegal things, rob, talk trash, go somewhere else")

    choice = input("Choose an action: ").strip().lower()

    if choice == "proceed":
        encounter = random.choice([True, False])
        if encounter:
            print("You encountered an enemy!")
            combat("Alley Opp", random.randint(30, 60), random.randint(5, 15))
        else:
            print("No enemies here.")

    elif choice == "hide":
        print("You hide successfully.")
    
    elif choice == "go somewhere else":
        location_selector()

    elif choice == "do illegal things":
        chance = random.randint(1, 10)
        if chance > (smarts_stat // 30) + (stealth_stat // 10):
            print("You did illegal things without getting caught.")
        else:
            money_stat -= 30
            street_respect_stat -= 20
            print("Caught! Lost money and respect.")
    elif choice == "rob":
        chance = random.randint(1, 10)
        if chance == 6:
            print("The person isn't giving up without a fight")
            combat("Random", random.randint(30, 100), random.randint(5, 20))
        elif chance == 7:
            money_stat -= 30
            street_respect_stat -= 20
            print("Caught! Lost money and respect.")
        elif chance == 8:
            money_stat -= 30
            street_respect_stat -= 20
            print("Caught! Lost money and respect.")
        else:
            money_stat += random.randint(0, 500)

            street_respect_stat += 15
            print(f"Robbery successful, you now have {money_stat} dollars, and {street_respect_stat} street respect.")
            
    else:
        print("Action not recognized.")

#DEFINE FUNCTION OUTSIDE():
def outside():
    print("\nYou are OUTSIDE.")
    print("Options: walk around, talk trash, go somewhere else")

    choice = input("Choose an action: ").strip().lower()

    if choice == "walk around":
        print("You stroll around the neighborhood.")
    elif choice == "talk trash":
        talk_trash_on_live()
    elif choice == "go somewhere else":
        location_selector()
    else:
        print("Action not recognized.")


#DEFINE FUNCTION HOSPITAL():
def hospital():
    global money_stat, health_stat

    print("\nYou are at the HOSPITAL.")
    print("Options: pay to recover health, talk trash, go somewhere else")

    choice = input("Choose an action: ").strip().lower()

    if choice == "pay to recover health fully":
        cost = 100
        if money_stat >= cost:
            money_stat -= cost
            health_stat = 100
            print("You paid and recovered to full health!")
        else:
            print("Not enough money to pay for health recovery.")
    elif choice == "talk trash":
        talk_trash_on_live()
    elif choice == "go somewhere else":
        location_selector()
    else:
        print("Action not recognized.")


#DEFINE FUNCTION OPPS_TERRITORY():
def opps_territory():
    global street_respect_stat

    print("\nYou entered OPP'S TERRITORY.")
    print("Prepare for combat!")

    combat("Opp Gang Leader", random.randint(80, 125), random.randint(10, 25))

    if health_stat > 0:
        print("You survived the opps territory.")
        location_selector()
    else:
        print("You lost in opps territory... Game over.")
        exit()



# ITEM SYSTEM

#DECLARE INVENTORY = STARTING ITEMS
inventory = {"Fists" : {"damage": fight_damage_stat}
             }

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
def combat(enemy_name, enemy_health, enemy_damage):
    global health_stat, street_respect_stat

    turn = "user"
    
    enemy_fight_choice = random.choice(["attack", "dodge"])
    user_fight_choice = random.choice(["attack", "dodge"])

    print(f"Oh no! You're getting jumped by {enemy_name}! - They have {enemy_health} and deal {enemy_damage} damage...")
    while enemy_health > 0 and health_stat > 0:
        if turn == "user":
            user_fight_choice = input("What do you want to do?: attack? - dodge? - run away? (type the word/words in letter for letter)").strip().lower()
            if user_fight_choice == "attack":
                attack_weapon_choice = input(f"Which weapon do you want to use from your? (type the word/words in letter for letter): {inventory}").strip().lower()

                if attack_weapon_choice in inventory:
                    enemy_health = enemy_health - "damage"
                    print(f"You did {"damage"} damage to {enemy_name}. - They now have {enemy_health}.")
                elif attack_weapon_choice == "fists":
                    enemy_health = enemy_health - fight_damage_stat
                    print(f"You did {fight_damage_stat} damage to {enemy_name}. - They now have {enemy_health} health.")
                    


            elif user_fight_choice == "dodge":
                user_dodge_success = random.randint(1, 5) #TWENTY PERCENT CHANCE DODGE FAILS
            elif user_fight_choice == "run away":
                user_escape_chance = random.randint(1, 10) #TEN PERCENT CHANCE ESCAPE FAILS
                if user_escape_chance == 6:
                    print(f"{enemy_name} snatched you before you could escape, and hit you!")
                    health_stat = health_stat - enemy_damage
                else:
                    street_respect_stat = street_respect_stat - 15
                    print(f"Imagine running from a fight like a scaredy cat. 💔\nThis is your street respect now though: {street_respect_stat}.")
                    break
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



# BOSS BATTLE SYSTEM SETUP

#DISPLAY INSTRUCTIONS:
# - SHADOW BOXING RULES:
#   * POINTER CHOOSES A DIRECTION TO POINT (UP, DOWN, LEFT, RIGHT)
#   * LOOKER MUST FOLLOW BY LOOKING IN THAT DIRECTION
#   * POINTER NEEDS TO GET THE LOOKER TO LOOK IN 3 DIFFERENT DIRECTIONS IN A ROW, EACH CORRECT FOLLOWING POINTER’S DIRECTION
#   * AFTER EACH SUCCESSFUL MATCH, THAT DIRECTION IS REMOVED FROM FUTURE POINTER CHOICES
#   * IF THE LOOKER LOOKS AWAY FROM THE POINTED DIRECTION, ROLES SWITCH (LOOKER BECOMES POINTER AND VICE VERSA)
#   * THE FIRST TO GET 3 SUCCESSFUL CONSECUTIVE DIRECTION MATCHES WINS

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

#DEFINE FUNCTION FINAL_BOSS_BATTLE():
def final_boss_battle():
    print("\nFINAL BOSS BATTLE: Shadow Boxing!")
    print("""
    Rules:
    - Pointer chooses direction (UP, DOWN, LEFT, RIGHT)
    - Looker must look in that direction
    - Pointer needs 3 correct consecutive matches, directions can't repeat
    - If Looker looks away, roles switch
    - First to 3 wins
    """)

    pointer = "player"  # 'player' or 'boss'
    looker = "boss"
    streak = 0
    allowed_directions = ["UP", "DOWN", "LEFT", "RIGHT"]

    while True:
        if pointer == "player":
            print(f"Allowed directions: {allowed_directions}")
            pointer_choice = input("Choose direction to point: ").strip().upper()
            while pointer_choice not in allowed_directions:
                pointer_choice = input("Invalid. Choose from allowed directions: ").strip().upper()
            # Boss randomly chooses look direction
            looker_choice = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
            print(f"Boss looks {looker_choice}")

        else:
            # Boss points
            pointer_choice = random.choice(allowed_directions)
            print(f"Boss points {pointer_choice}")
            # Player looks
            looker_choice = input("Look in which direction? ").strip().upper()
            while looker_choice not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                looker_choice = input("Invalid. Look UP, DOWN, LEFT or RIGHT: ").strip().upper()

        if pointer_choice == looker_choice:
            streak += 1
            allowed_directions.remove(pointer_choice)
            print(f"Match! Current streak: {streak}")

            if streak == 3:
                print(f"{pointer.capitalize()} wins the shadow boxing!")
                break
        else:
            print("Looker looked away! Roles switch!")
            pointer, looker = looker, pointer
            streak = 0
            allowed_directions = ["UP", "DOWN", "LEFT", "RIGHT"]

    if pointer == "player":
        print("Congratulations! You won the final boss battle!")
    else:
        print("You lost the final boss battle... Game over.")
        exit()


# END OF GAME

#IF PLAYER SURVIVES ALL 7 DAYS AND DEFEATS BOSS:
#     DISPLAY ENDING AND CREDITS
def game_ending():
    print("\nCongratulations! You survived the week and defeated the boss!")
    print("Thanks for playing Free Game Based in the Hood!")
    print("Game developed by Gov fr.")


#IF PLAYER_HEALTH IS LESS THAN OR EQUAL TO 0 AT ANY TIME:
#     DISPLAY GAME OVER MESSAGE
def check_player_health():
    global health_stat
    if health_stat <= 0:
        print("You died - Game Over!!!")
        exit()

# TIME / DAY LOOP SYSTEM

#DECLARE DAY = 1
day = 1

#WHILE DAY IS LESS THAN OR EQUAL TO 7:
while day <= 7:

    #DISPLAY CURRENT DAY NUMBER
    print(f"\n====================")
    print(f"DAY {day}")
    print(f"====================")

    #DECLARE ACTIONS_TAKEN = 0
    actions_taken = 0

    #WHILE ACTIONS_TAKEN IS LESS THAN 3:
    while actions_taken < 3:

        #CALL LOCATION_SELECTOR FUNCTION TO ALLOW PLAYER ACTIONS
        location_selector()

        #IF PLAYER_HEALTH IS LESS THAN OR EQUAL TO 0:
        if health_stat <= 0:
            print("You died. GAME OVER.")
            exit()

        #INCREMENT ACTIONS_TAKEN BY 1
        actions_taken += 1

        #DISPLAY ACTIONS LEFT IN THE DAY
        print(f"Actions left today: {3 - actions_taken}")

    #INCREMENT DAY BY 1 AFTER 3 ACTIONS
    day += 1


#WHEN DAY REACHES 8 (END OF WEEK):
if day > 7:
    print("\nYou've made it to the end of the week...")
    print("Your big bro has been waiting for you.")
    final_boss_battle()



# ACTIONS LIST

#actions = [
 #   "HANG AROUND",
  #  "GOOF OFF",
   # "TALK TRASH TO OPPS ON LIVE",
    #"ROB SOMEONE/PLACE",
    #"EAT/BUY SOMETHING",
    #"HIDE THERE"
#]