# GNB - 1st - 🔨 Order Up!

menu = {
    "Drinks" : {
        "Water" : 0.00,
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
    }
}

print("Hello, User! Welcome to a place to get food!")

# Function for user validation
def choose_item(category, prompt):
    while True:
        print(f"The {category} Menu:")
        for item, price in menu[category].items():
            print(f"{item}: ${price}")

        choice = input(f"{prompt}").strip()

        if choice in menu[category]:
            return choice
        else:
            print("Invalid choice. Please pick something from the menu.")


# User selects drink
drink_choice = choose_item("Drinks", "What drink would you like to have? ")


# User selects main course (Entrée)
entree_choice = choose_item("Entrées", "What entrée would you like? ")


# User selects two sides
side_choice1 = choose_item("Sides", "Choose your first side: ")
side_choice2 = choose_item("Sides", "Choose your second side: ")

# calculate total of order
order = {
    "Drink": drink_choice,
    "Entrée": entree_choice,
    "Side 1": side_choice1,
    "Side 2": side_choice2
}

total_cost = (
    menu["Drinks"][drink_choice] +
    menu["Entrées"][entree_choice] +
    menu["Sides"][side_choice1] +
    menu["Sides"][side_choice2]
)


# Display order summary
print("Full Order Summary: ")
for category, item in order.items():
    # find correct price
    if category == "Drink":
        price = menu["Drinks"][item]
    elif category == "Entrée":
        price = menu["Entrées"][item]
    else:
        price = menu["Sides"][item]

    print(f"{category}: {item} - ${price}")

print(f"Total Cost: ${total_cost:.2f}")
print("Thanks for ordering! Have a blessed day!")
