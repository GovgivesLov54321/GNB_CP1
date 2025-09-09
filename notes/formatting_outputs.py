# GNB - 1st - ☑️Formatting Outputs Notes

name = "Nombre"
age = 9023533749027867
money = 225436543765734756876767676767.4298039876023
percentage = .67

print("Hello {}, you are {:,}?! That's so old, but at least you have ${:,}. Random percentage *gasp*: {:%}".format(name, age, money, percentage))

print(f"Hello {name}, you are {age:,}. That's so old, but at least you have ${money:,}. The random percentage is *gasp*: {percentage:%}.")