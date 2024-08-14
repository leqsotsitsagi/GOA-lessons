# 1.

elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

print("Positive Indexing:")
for i in range(len(elements)):
    print(f"Index {i}: {elements[i]}")

print("\nNegative Indexing:")
for i in range(-len(elements), 0):
    print(f"Index {i}: {elements[i]}")

# 2.

new_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

print("First three elements:", new_list[:3])
print("Second three elements:", new_list[3:6])
print("Third three elements:", new_list[6:9])
print("Fourth three elements:", new_list[9:12])
print("Fifth three elements:", new_list[12:])

# 3.

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Initial List:", my_list)

my_list[0] = 'apricot'
my_list[1] = 'blueberry'
my_list[2] = 'cranberry'
my_list[3] = 'dragonfruit'
my_list[4] = 'fig'

print("Modified List:", my_list)

# 4.

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Initial List:", my_list)

my_list[1:3] = ['blueberry', 'cranberry']

print("Modified List:", my_list)
