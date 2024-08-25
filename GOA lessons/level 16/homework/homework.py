# 1.

def output_range(start, end):
    for i in range(start, end + 1):
        print(i)

output_range(1, 5)

# 2.

def introduce(first_name, last_name, age, academy):
    print(f"My name is {first_name}, my surname is {last_name}, I study in {academy}.")

introduce("leqso", "tsitsagi", 15, "GOA(goal oriented academy)")

# 3.

def greet(first, last):
    print(f"hello {first} {last}")

greet("leqso", "tsitsagi")

# 4.

def sum(a, b):
    return(a + b)

result = sum(5, 3)
print(result)

# 5.

def samravli(A, B, C):
    return(A * B * C)

namravli = samravli(3, 4, 5)
print(namravli)

# 6.

def list_food(snacks):
    for food in snacks:
        print(food)

food_list = ["Chips", "Cookies", "Popcorn", "Candy"]
list_food(food_list)