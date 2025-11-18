# GNB - 1st - 🔨 Flexible Calculator


print("Welcome to the Flexible Calculator.\nThe avaiable operations that can be calculated are Sum, Average, Maximum, Minimum, or Product.")
while True:
    operation_choice = input("Which operation would you like to be performed?:\n").strip().capitalize()
    if operation_choice == "Sum" or operation_choice == "Average" or operation_choice == "Maximum" or operation_choice == "Minimum" or operation_choice == "Product":
        print("Great choice!")
    else:
        print("Not an option, buddy.")
        continue
   

    num_choices = input("Enter a number (enter done, when done):\n")

    if num_choices == "done":
        break    
    elif num_choices == 0:
        print("Cool number")
    else:
        print("Not an option, buddy. Try again.")

    def calculations(sum, average, maximum, minimum, product):
        sum = (num_choices + num_choices)
    calculations()

    if num_choices == "done":
        print(calculations(f"The sum of the numbers you gave is {sum}"))