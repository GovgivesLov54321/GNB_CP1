# GNB - 1st - Final Project
#IMPORT RANDOM LIBRARY
import random

#WELCOME USER TO “FREE GAME BASED IN THE HOOD”
print("Welcome, User, to a Free Game Based in the Hood!")
#EXPLAIN:
print("In this game, you'll experience life as you have relationships (best friend, significant other, etc.), know what it's kind of like to be part of a gang, and fight your big bro in a final battle of shadow boxing.\nYou'll be living a week in the life; everyday you'll have the option to go to at most three different places (or even just stay at the same place) and do some things there.\nYou can live out the entire week, if you don't die...death = GAME OVER!")
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

#DECLARE INVENTORY = EMPTY LIST
inventory = ["Fists"]

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
def modify_stats(stat_value, amount):
    stat_value = stat_value + amount

#DEFINE FUNCTION PICKUP_ITEM(item):
#     IF item HAS NOT ALREADY BEEN PICKED UP:
#          ADD item TO INVENTORY
#          APPLY THE RELEVANT STAT BOOST TO PLAYER
#          MARK item AS PICKED UP
def pickup_items(item_picked, item, stat_value, amount):
    if item_picked == False:
        inventory.append(item)
        item_picked = True
        modify_stats()

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
def combat_system(enemy_name, enemy_health, enemy_damage, attack_weapon_choice):
    enemy_damage = random.randint(5, 16)
    enemy_health = random.randint(50, 175)
    print(f"Oh no! You're getting jumped by {enemy_name}!")
    user_fight_choice = input("What do you want to do?: attack? - dodge? - run away? (type the word/words in letter for letter)").strip().lower()
    if user_fight_choice == "attack":
        attack_weapon_choice = input(f"Which weapon do you want to use?: {inventory}")
        enemy_health = enemy_health - a

    elif user_fight_choice == "dodge":
        dodge_success = random.randint(1, 2)
        if dodge_success == 1:
            print("You dodged successfully!")
        else:
            print("Imagine trying to dodge, and still getting hit. 💀")
    elif user_fight_choice == "run away":
        escape_chance = random.randint(1, 10)
        if escape_chance == 6:
            print(f"{enemy_name} snatched you before you could escape, and hit you!")
            health_stat = health_stat - {enemy_damage}
        else:
            print("Imagine running from a fight like a scaredy cat. 💔")
            street_respect_stat = street_respect_stat - 15





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
#DECLARE COMP_ISH_DIRECTIONS = ["UP","DOWN","LEFT","RIGHT"]

#DECLARE USER_ISH_CHOICE = USER INPUT (SELECT DIRECTION FROM ALLOWED OPTIONS)
#DECLARE COMP_ISH_CHOICE = RANDOMLY SELECTED FROM COMP_ISH_DIRECTIONS

#DECLARE COINFLIP:
# USER CHOOSES HEADS OR TAILS
# RANDOM RESULT DECIDES WHO GOES FIRST


# DICTIONARIES FOR CHARACTERS

#DECLARE CHARACTERS DICTIONARY:
# "BEST FRIEND": "LEBRONITO"
# "SIGNIFICANT OTHER": "PO"
# "GANG LEADER": "REGINALD"
# "BIG BROTHER": "JEREMIAH"
# "OPP GANG LEADER": "JUJU-LAWRENCE"
# "HOMELESS MAN": "JARVIS"
# "HOMELESS WOMAN": "CECE"


# LOCATIONS LIST

#DECLARE LOCATIONS:
# HOME
# BESTIE_HOME
# SIGNIFICANT_OTHER_HOME
# GANG_SPOT
# MCDONALDS
# GAS_STATION
# ALLEYWAY
# OUTSIDE
# HOSPITAL
# OPPS_TERRITORY

# ITEMS WITH DAMAGE (ONLY CAN BE FOUND IN RANDOM PLACES) LIST

#DICTIONARY WITH ITEM NAMES TO DAMAGE:
# MACHETE : 10
# PISTOL : 16
# PEPPER SPRAY : 4
# BRASS KNUCKLES : RANDOM FROM 7-13
# GRENADE : 67

# ITEMS WITH DAMAGE (ONLY CAN BE BOUGHT OFF AMAZON) LIST

#DICTIONARY WITH ITEM NAMES/DAMAGE TO PRICE:
# KATANA/17DMG : 30
# DRACO (GUN)/20DMG : 50
# WOLVERINE CLAWS/15DMG : 42
# ROCKET LAUNCHER/75DMG : 567
# FLASHBANG/20DMG : 67

# ACTIONS LIST

#DECLARE ACTIONS:
# HANG AROUND
# GOOF OFF
# TALK TRASH TO OPPS ON LIVE
# ROB SOMEONE/PLACE
# EAT/BUY SOMETHING
# HIDE THERE


# LOCATION FUNCTIONS

#DEFINE FUNCTION HOME():
#     DISPLAY OPTIONS TO PLAYER:
#     - SLEEP
#     - EAT
#     - PLAY GAMES
#     - INVITE BEST FRIEND
#     - INVITE SIGNIFICANT OTHER
#     - READ (INCREASE SMARTS)
#     - ORDER WEAPON FROM AMAZON
#     - GO SOMEWHERE ELSE
#     - TALK TRASH TO OPPS ON LIVE
#     - HIDE THERE

#     IF USER CHOOSES READ:
#          INCREASE SMARTS STAT BY A CERTAIN AMOUNT

#     IF USER CHOOSES ORDER WEAPON:
#          CALL PICKUP_ITEM WITH BASIC WEAPON

#     IF USER CHOOSES GO SOMEWHERE ELSE:
#          CALL LOCATION_SELECTOR FUNCTION TO CHOOSE NEW LOCATION

#DEFINE FUNCTION BESTIE_HOME():
#     DISPLAY OPTIONS:
#     - SLEEP
#     - EAT
#     - HANG OUT
#     - READ (INCREASE SMARTS)
#     - ORDER WEAPON
#     - GO SOMEWHERE ELSE
#     - TALK TRASH TO OPPS ON LIVE

#DEFINE FUNCTION SIGNIFICANT_OTHER_HOME():
#     SAME OPTIONS AS BESTIE_HOME, PLUS THE OPTION TO HIDE THERE

#DEFINE FUNCTION GANG_SPOT():
#     DISPLAY OPTIONS:
#     - HANG OUT
#     - READ (INCREASE SMARTS)
#     - ORDER WEAPON
#     - GO SOMEWHERE ELSE
#     - TALK TRASH TO OPPS ON LIVE
#     - HIDE THERE

#DEFINE FUNCTION WORK_MCDONALDS():
#     PLAYER EARNS MONEY BASED ON WORK
#     IF PLAYER SKIPS WORK:
#          DECREASE STREET_RESPECT

#DEFINE FUNCTION GAS_STATION():
#     PLAYER CAN BUY FOOD
#     PLAYER CAN CHOOSE TO ROB
#     IF PLAYER IS CAUGHT ROBBING:
#          LOSE MONEY AND STREET_RESPECT

#DEFINE FUNCTION ALLEYWAY():
#     RANDOM CHANCE OF ENCOUNTER
#     MAY TRIGGER EXTRA COMBAT ONCE
#     PLAYER CAN CHOOSE TO HIDE OR PROCEED
#     PLAYER CAN CHOOSE TO DO ILLEGAL THINGS WITH RISK OF GETTING CAUGHT
#     IF PLAYER IS CAUGHT:
#          LOSE MONEY AND STREET_RESPECT
#     PLAYER CAN ROB A PERSON
#     IF PLAYER’S SMARTS OR STEALTH IS LOW:
#          HIGHER CHANCE OF GETTING CAUGHT AND LOSING MONEY

#DEFINE FUNCTION OPPS_TERRITORY():
#     TRIGGERS EXTRA COMBAT SCENE (NON-BOSS)
#     ENEMY DOES NOT RESPAWN
#     INCREASE STREET_RESPECT ON VICTORY

#DEFINE FUNCTION HOSPITAL():
#     PLAYER CAN PAY MONEY TO RECOVER HEALTH


# LOCATION SELECTOR

#DEFINE FUNCTION LOCATION_SELECTOR():
#     DISPLAY ALL LOCATIONS TO PLAYER
#     PLAYER CHOOSES ONE
#     CALL THE CORRESPONDING LOCATION FUNCTION


# TIME/DAY LOOP

#DECLARE DAY = 1

#WHILE DAY IS LESS THAN OR EQUAL TO 7:
#     DISPLAY CURRENT DAY NUMBER
#     CALL HOME FUNCTION TO ALLOW PLAYER ACTIONS
#     AFTER PLAYER COMPLETES 3 ACTIONS:
#          INCREMENT DAY BY 1


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