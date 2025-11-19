# GNB - 1st - ☑️Mapping Notes

numbers = [67, 6767, 6, 7, 676767, 5, 54, 567]
"""new_nums = []

for number in numbers:
    new_nums.append(number/3)

print(new_nums)"""
def divide(num):
    return num/3 #Returns location & heap

new_nums = map(divide, numbers)
print(new_nums)
for num in new_nums:
    print(num)

new_nums = map(lambda num: num/3, numbers) #Shortens previous function
print(new_nums)
for num in new_nums:
    print(num)