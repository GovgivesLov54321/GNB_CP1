# GNB - 1st - 🔨 What is My Grade

grade = float(input("What's your percentage grade in English 10H (don't include '%' sign)?: \n"))

if grade >= 94:
    print("Great job, kiddo! You've got an A in English!")
elif grade >= 90 and grade < 94:
    print("Great job, kiddo! You've got an A- in English!")
elif grade >= 87 and grade < 90:
    print("Exceptional job, cuz! You have a B+ in English!")
elif grade >= 84 and grade < 87:
    print("Exceptional job, dude! You've got a B in English!")
elif grade >= 80 and grade < 84:
    print("Nice job, kiddo! You've got a B- in English!")
elif grade >= 77 and grade < 80:
    print("Uh, maybe you should lock in, bro. You have a C+ in English!")
elif grade >= 74 and grade < 77:
    print("Yeah lock in, man. You've got a C in English!")
elif grade >= 70 and grade < 74:
    print("Yikes! You've got a C- in English!")
elif grade >= 67 and grade < 70:
    print("Bro, please lock in 🙏! You've got a D+ in English!")
elif grade >= 64 and grade < 67:
    print("What are you doing with your life 😭?! You've got a D in English!")
elif grade >= 60 and grade < 64:
    print("Yeah I think it's ggs, big bro 🤦. You've got a D- in English.")
else:
    print("Yeah you're chopped cheese, buddy 🥀💀. You've got an F in English...")