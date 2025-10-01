# GNB - 1st - ☑️For Loops Notes

import time

nums = [4, 543, 652, 56, 67, 3241 , 534, 654754, 124, 6, 5464, 234]
# make variable for list plural version of word 
for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. it is a large number!")
    else:
        print(num)

print("The loop is over...")

for num in range(1, 11, 2): #It's : (start point, end point, increment - aka how much it'll count by)
    print(num)


for num in range(20, 0, -2):
    print(num)