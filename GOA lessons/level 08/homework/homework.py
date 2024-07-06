num1 = input("type a number: ")
num2 = input("type another number: ")

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)

print(10 > 5) #True
print(8 > 7) #True
print(15 > 10) #True
print(5 < 10) #True
print(7 < 8) #True
print(15 < 10) #False
print(5 == 5) #True
print(10 == 10) #True
print(15 == 10) #False
print(15 != 10) #True
print(10 != 5) #True
print(5 != 15) #True
print(15 <= 15) #True
print(10 <= 5) #False
print(5 <= 5) #True
print(15 >= 20) #False
print(10 >= 5) #True
print(5 >= 5) #True

reassign = 90
norm = 75
print(reassign > norm) #True
reassign = 60
print(reassign > norm) #False