# GNB - 1st - ☑️While Loops Notes
import random

num = 1

for num in range(1,21):
    print(num)

#while num <= 20:
    #print(num)
    #num += 1
# infinite loop
while num <= 20:
    print(1)
    num += 1 # stops infinite loop

goose = random.randint(1,20)
count = 0

while count == goose:
    count += 1 
    print("duck")
    if count == 6:
        break
else: 
    print("GOOSE!!!")

print("The code is done!")

i = 0

while i < 20:
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop.0")
    i += 1
print("The loop ended!")