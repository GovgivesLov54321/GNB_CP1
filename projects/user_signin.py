# GNB - 1st - 🔨 User Sign In

true_user = "vienna.larose@ucas-edu.net"
true_password = "he_a_g00fy-goob3R"
username = input("Enter username: \n")
password = input("Enter password: \n")

if username != true_user and password != true_password:
    print("Username and password are invalid")
elif username != true_user or password != true_password:
    print("Username or password is invalid")
else:
   print("Welcome to the program, Comrade ☭.")

# this is the username: vienna.larose@ucas-edu.net
# this is the password: he_a_g00fy-goob3R