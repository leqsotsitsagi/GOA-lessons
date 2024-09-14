# String functions
text = "Hello World"

# .upper() - Makes all letters uppercase.
upper_text = text.upper()
print(upper_text)

# .lower() - Makes all letters lowercase.
lower_text = text.lower()
print(lower_text)

# .capitalize() - Makes the first letter uppercase.
capitalized_text = text.capitalize()
print(capitalized_text)

# .swapcase() - Switches uppercase to lowercase and vice versa.
swapped_text = text.swapcase()
print(swapped_text)

# .find() - Finds the position of the first occurrence of a letter.
index_of_w = text.find("W")
print(index_of_w)

# len() - Tells how many characters (or items) are in the string (or list).
length = len(text)
print(length)

# .index() - Finds where a letter first appears in the string.
index_of_o = text.index("o")
print(index_of_o)

# List functions
numbers = [1, 2, 3, 4, 5]

# .append() - Adds an item to the end of the list.
numbers.append(6)
print(numbers)

# .insert() - Adds an item at a specific spot in the list.
numbers.insert(2, 10)
print(numbers)

# .pop() - Removes the last item (or a specific item) from the list.
popped_item = numbers.pop()
print(popped_item)
print(numbers)

# .remove() - Removes the first occurrence of a specific value.
numbers.remove(10)
print(numbers)
