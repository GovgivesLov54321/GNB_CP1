# GNB - 1st - 🔨 Average Grade
first = int(input("Good day! What's the grade percentage of your first period class?: \n"))

second = int(input("Good day! What's the grade percentage of your second period class?: \n"))

third = int(input("Good day! What's the grade percentage of your third period class?: \n"))

fourth = int(input("Good day! What's the grade percentage of your fourth period class?: \n"))

fifth = int(input("Good day! What's the grade percentage of your fifth period class?: \n"))

sixth = int(input("Good day! What's the grade percentage of your sixth period class?: \n"))

seventh = int(input("Good day! What's the grade percentage of your seventh period class?: \n"))

avg_grade = (first+second+third+fourth+fifth+sixth+seventh)/7

avg_grade = round(avg_grade, 2)

print("WOW!!! Your average grade is", str(avg_grade) +"%!")