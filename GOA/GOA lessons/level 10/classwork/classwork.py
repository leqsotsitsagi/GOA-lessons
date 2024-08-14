# 1.

number = 15
print(10 < number < 20)  # True

number = 25
print(number < 10 or number > 20)  # True

number = 4
print(number % 2 == 0 and number > 0)  # True

number = -3
print(number % 2 != 0 or number < 0)  # True

char = 'e'
print(char in 'aeiouAEIOU')  # True

char = 'b'
print(char not in 'aeiouAEIOU')  # True

string = ""
print(not string)  # True

string = "   "
print(string.isspace())  # True

a, b = 5, 10
print(a > 0 and b > 0)  # True

a, b = -5, 10
print(a > 0 or b > 0)  # True

my_list = [1, 2, 3]
print(bool(my_list))  # True

number = 3
print(number in my_list)  # True

my_list = [1, 2, 3, 4]
print(all(x > 0 for x in my_list))  # True

my_list = [1, -2, 3, 4]
print(any(x < 0 for x in my_list))  # True

string = "hello"
print(string.startswith('h'))  # True

string = "world"
print(string.endswith('d'))  # True

str1, str2 = "Hello", "hello"
print(str1.lower() == str2.lower())  # True

number = 15
print(number % 3 == 0 and number % 5 == 0)  # True

number = 10
print(number % 3 == 0 or number % 5 == 0)  # True

a, b = 5, 10
print(a != b)  # True

# 2.

for i in range(1, 101):
    print(i)

# 3.

for i in range(1, 11):
    if i == 1:
        continue
    print(i)

# 4.

for i in range(100, 0, -1):
    print(i)

# 5.

i = 1
while i <= 100:
    print(i)
    i += 1

# 6.

i = 1
while i <= 10:
    if i == 1:
        i += 1
        continue
    print(i)
    i += 1

# 7.

i = 100
while i >= 1:
    print(i)
    i -= 1
