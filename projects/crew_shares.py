# GNB - 1st - 💡Crew Shares

crew_num = int(input("How many people are a part of the crew? (not including the captain and first mate): "))
last_outing = float(input("So how much money did the crew last make? (give a number): "))

caps_share = float(round((last_outing * (7/(crew_num + 2))), 2))
print(caps_share)

first_mate_share = float(round((last_outing * (3/(crew_num + 2 ))), 2))
print(first_mate_share)

crews_share = float(round((last_outing * (1/(crew_num + 2 ))) - 500, 2))
print(crews_share)