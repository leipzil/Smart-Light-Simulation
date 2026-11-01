short = int(input("Enter the number of short-answer questions already completed: "))
essay = int(input("Enter the number of essay questions already completed: "))
remaining = 60 - (14-short)*10 - (2-essay)*20
if remaining < 0:
    print("Mr. Riz will not complete all questions")
else:
    print("Mr. Riz will successfully complete all questions")

number = int(input("Enter a number: "))
numbers = str(number)
total = numbers[0] + numbers[1]) + numbers[2] + numbers[3]
if total % int(numbers[0] == 0  and total % numbers[1] and total % numbers[2] and total % numbers[3]:
    print("The number is a bravo number")
else:
    print("The number is an ordinary number")