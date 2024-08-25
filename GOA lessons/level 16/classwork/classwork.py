# 1.

def greet_world():
    return "Hello world!"

# 2.

def greet_person(name):
    return f"Hello {name}!"

# 3.

def product_of_two_numbers(a, b):
    return a * b

# 4.

def sum_of_three_numbers(a, b, c):
    return a + b + c

# 5.

def is_of_legal_age(age, legal_age=18):
    if age >= legal_age:
        return True
    else:
        return False

# 6.

def check_pass(score):
    if score > 80:
        return "Passed"
    else:
        return "Not Passed"
