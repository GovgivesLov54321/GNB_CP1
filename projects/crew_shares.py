# GNB - 1st - 💡Crew Shares

crew_num = int(input("How many people are a part of the crew? (not including the captain and first mate): \n"))
last_outing = float(input("So how much money did the crew last make? (give a number): \n"))

divider = crew_num + 10
shares = last_outing / divider

caps_share = shares * 7
print(f"The captain will receive ${caps_share:.2f}")

first_mate_share = shares * 3
print(first_mate_share)

precrews_share = shares
crew_shares = precrews_share - 500
print(crew_shares)