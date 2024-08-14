# 1.

i = 1

while i <= 100:
    if i < 50 or i > 60:
        print(i)
    i += 1

# 2.

i = 1
answer = 0

while answer < 50:
    answer += i
    print(answer)
    i += 1

# 3.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 4.

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    grade = "Grade A"
elif 80 <= score <= 89:
    grade = "Grade B"
elif 70 <= score <= 79:
    grade = "Grade C"
elif 60 <= score <= 69:
    grade = "Grade D"
elif 0 <= score <= 59:
    grade = "Grade F"
else:
    grade = "Invalid score"

print(f"Your score is {score}. {grade}.")

# 5.

age = int(input("enter your age: "))
if age < 13:
    print("you are a kid")
elif 13 <= age < 20:
    print("you are a teenager")
else:
    print("you are an adult")