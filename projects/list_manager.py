# GNB - 1st - 🔨 Shopping List Manager

shop_list = []

while True:
    print("Would you like to: \n 1. Add item to list \n 2. Remove an item from list \n 3. Print out list")
    choice = input("Choose an option (1-3):\n")
    if choice == "1":
        add = input("What would you like to add to your shopping list, User? (one item at a time):\n")
        shop_list.append(add)

    elif choice == "2":
        clear = input("Would you like to completely empty your list? (Yes or No):\n")
        if clear == "Yes":
            shop_list.clear()
        elif clear == "No":
            pass
            print(shop_list)
            remove = input("What item would you like to remove from your shopping list, User? (enter Cancel to go back to options):\n")
            if remove == "Cancel":
                continue
            shop_list.remove(remove)
        else: print("That is not an option.")

    elif choice == "3":
        double_check = input("Are you sure you would like to end, and print your list? (Yes or No):\n")
        if double_check == "Yes":
            print(f"This is your final list!:\n{shop_list}")
            break
        elif double_check == "No":
            True
        else: print("That is not an option.")
    else: print("That is not an option")