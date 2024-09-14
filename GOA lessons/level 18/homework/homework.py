# 1.

a = 5
b = 10
print(a + b)

# 2.

str1 = "hello"
str2 = "world"
print(str1.upper(), str2.upper())

# 3.

x = 20
y = 4
print(x / y) 

# 4.



# 5.

print(5 + 5 == 8 + 2)

# 6.

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

# 7.

print(5 > 3 and 10 > 2)
print(5 < 3 or 10 > 2)
print(5 == 5 and 10 < 5)
print(not(5 > 10))
print(7 > 4 or 4 > 8 and 6 < 10)

# 8.

for i in range(1, 11):
    print(i)

# 9.

numbers = [1, 2, 3, 4, 5]
total_sum = 0
for num in numbers:
    total_sum += num
print(total_sum)

# 10.

for char in "Hello, World!":
    print(char)

# 11.

i = 1
while i <= 10:
    print(i)
    i += 1

# 12.

i = 1
while i <= 100:
    if 50 <= i <= 60:
        print(i)
    i += 1

# 13.

i = 1
total = 0
while total < 50:
    total += i
    i += 1
print(total)

# 14.

def check_divisibility():
    number = int(input("Enter a number: "))
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5")
    elif number % 3 == 0:
        print("Divisible by 3")
    elif number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 3 or 5")

# 15.

numbers = [1, 3, 4, 5, 2]
print(numbers[1])

# 16.

s = "Hello"
new_str = s[:-1] + s[-1].upper()
print(new_str)

# 17.

numbers = [3, 12, 5, 2, 6]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# 18.

text = "Hello World"

upper_text = text.upper()
print(upper_text)

lower_text = text.lower()
print(lower_text)

capitalized_text = text.capitalize()
print(capitalized_text)

swapped_text = text.swapcase()
print(swapped_text)

index_of_w = text.find("W")
print(index_of_w)

length = len(text)
print(length)

index_of_o = text.index("o")
print(index_of_o)

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)

numbers.insert(2, 10)
print(numbers)

popped_item = numbers.pop()
print(popped_item)
print(numbers)

numbers.remove(10)
print(numbers)