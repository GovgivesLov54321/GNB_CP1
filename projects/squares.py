# GNB - 1st - 🔨 Squared Numbers
nums = [5, 7, 8, 12, 25, 30, 45, 50, 65, 67, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285, 67676767676767676767676767]

squared_nums = list(map(lambda num: num*num, nums))
for num in nums:
    print(f"OG numbers: {num}, Squared numbers: {squared_nums[nums.index(num)]}")