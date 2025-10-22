# GNB - 1st - ☑️Functions Notes
#Set variables
player_health = 100
monster_health = 100
#define functions
def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount

monster_health, player_health= damage(10, "player")
print(monster_health)
print(player_health)
def add(x, y):
    #print(f"{x}+{y} = {x+y}")
    return x + y

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name [0]

    return initials

total = add(5,5)
print(total)
print(f" 10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("duck")
    x += 1

print("Goose")

print(initials("Tia LaRose"))
print(initials("Franco Barboza"))

#ASCII caca frfr
print(f"c = {ord("c")}")
print(f"67 = {chr(67)}")
























