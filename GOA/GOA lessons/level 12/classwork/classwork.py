# 1.

age = int(input("enter your age: "))
if age >= 18:
    print("regular price")
else:
    print("discount")

# 2.

number = int(input("Enter your number: "))
if number == 6:
    print("You won a house!")
elif number == 30:
    print("You won a ticket to Hawaii!")
else:
    print("You won 1 dollar")

# 3.

age = int(input("enter your age: "))
isstudent = True
if age < 18 or isstudent == True:
    print("discount")