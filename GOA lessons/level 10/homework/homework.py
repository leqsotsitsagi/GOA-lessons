for i in range(1, 11):
    print(i)
    print("Hello world!")

total_sum = 0
for i in range(1, 11):
    total_sum += i
print("The sum is:", total_sum)

for i in range(1001):
    if i == 100:
        continue
    print(i)

for i in range(100, -1, -1):
    print(i)

i = 1
while i <= 10:
    print(i)
    print("Hello world!")
    i += 1

total_sum = 0
i = 1
while i <= 10:
    total_sum += i
    i += 1
print("The sum is:", total_sum)

i = 0
while i <= 1000:
    if i == 100:
        i += 1
        continue
    print(i)
    i += 1

i = 100
while i >= 0:
    print(i)
    i -= 1
