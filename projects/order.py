# GNB - 1st - 🔨 Order Up!

tax_per = .0585
menu = {
    "Drinks" : {
        "Water" : "Free",
         "Fresh Fruit Juice": 3.00,
         "Sparkling Water" : 2.00,
         "Soda Cup" : 2.75,
         "Vanilla Milkshake" :  3.25,
         "Strawberry Milkshake" : 3.25,
         "Chocolate Milkshake" : 3.25,
         "Horchata" : 3.70
    },
    "Entrées" : {
         "Bean & Cheese Burrito" : 2.99,
         "Bean Burrito" : 2.50,
        "Bacon, Egg, Potatoes, & Cheese Burrito" : 3.55,
         "Bacon & Egg Burrito" : 3.30,
         "Potato & Egg Burrito" : 3.25,
         "Bacon & Potato Burrito" : 3.25,
         "Egg Burrito" : 3.00,
         "Steak, Egg, Potatoes, & Cheese Burrito" : 3.70,
         "Steak & Egg Burrito" : 3.45,
         "Steak & Potato Burrito" : 3.45,
         "Chorizo, Egg, Potatoes, & Cheese Burrito" : 3.80,
         "Chorizo & Egg Burrito" : 3.60,
         "Chorizo & Potato Burrito" : 3.25,
         "The Everything Burrito" : 67.67,
         "Chilaquiles Verdes/Rojos" : 7.50,
         "Gameday Nacho Plate" : 7.00
    },
    "Sides" : {
         "Chips" : 3.75,
         "(Spicy) Breakfast Potatoes" : 4.75,
         "Salsa Roja" : 2.00,
         "Salsa Verde" : 2.25,
         "Guacamole" : 3.00,
         "Sour Cream" : 1.75,
         "Flour/Corn Tortilla" : 2.00,
         "Black Beans" : 3.00,
         "Pinto Beans" : 3.00,
         "Refried Black Beans" : 3.75,
         "Refried Pinto Beans" : 3.75,
         "Plantain Chips" : 4.00
    },
    "Desserts" : {
         "Tres Leches Cake Slice" : 6.00,
         "Ice Cream" : 5.00,
         "Chocolate Chip Cookies" : 4.50,
         "Flan Slice" : 5.00,
         "Banana Pudding" : 6.55,
         "Churros" : 6.40,
         "Cinnamon/Strawberry/Cheese Cheesecake Slice" : 5.65
    }
}
print("Hello, User! Welcome to a place to get food!")


print("The Drink Menu:")
for menu['Drink'] in menu["Drinks"]:
     print(f"{menu["Drink"]}")

drink_choice = input(f"What drink would you like to have: \n").strip()

if drink_choice == "Water":
     print(f"Water is {menu['Drinks']['Water']}")
elif drink_choice == "Fresh Fruit Juice":
     print(f"Fresh Fruit Juice costs ${menu['Drinks']['Fresh Fruit Juice']}")



#for menu['Drink'] in menu['Drinks']:
            #print(f"{menu['Drink']} costs {menu['Drinks'[value]]}")



