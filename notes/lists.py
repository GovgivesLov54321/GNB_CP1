# GNB - 1st - ☑️Lists Notes
import random

sibs = ["Pedro", "Pace", "ID"]
print(sibs[0])
print(f"The list is {len(sibs)} people long.")
sibs[0] = "Juan"
print(sibs)
sibs[1:2] = ["Jose", "Lebooboo"]
print(sibs)
sibs.pop() #removes the item at the end of the list
sibs.pop(2) #OR sibs.remove("name") ALSO sibs.clear() to remove everything
print(sibs)
sibs.append("ID")
print(sibs)
sibs.insert(1, "Pace")
print(sibs)
sibs.extend(["Braxton", "Benjamin", "Maggie"])
print(sibs)
print(random.choice(sibs))

board = [[1,2,3],
         [4,5,6],
         [7,8,9]
        ]

fruit = ("Apple", "Orange", "Pinapple") #tuple ordered, not changeable

veggies = {"Potato", "Cilantro", "Radish"} #set unordered, changeable
print(veggies)
veggies.clear
print(veggies)
print(board)