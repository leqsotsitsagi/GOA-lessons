# 1.

list1 = ['apple', 'banana']
list2 = ['cat', 'dog', 'elephant']
list3 = ['red', 'blue', 'green', 'yellow']
list4 = ['one', 'two', 'three', 'four', 'five']
list5 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print("List 1 (Positive):", list1[:])
print("List 1 (Negative):", list1[::-1])

print("List 2 (Positive):", list2[:])
print("List 2 (Negative):", list2[::-1])

print("List 3 (Positive):", list3[:])
print("List 3 (Negative):", list3[::-1])

print("List 4 (Positive):", list4[:])
print("List 4 (Negative):", list4[::-1])

print("List 5 (Positive):", list5[:])
print("List 5 (Negative):", list5[::-1])

# 2.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sum_second_last = numbers[1] + numbers[-1]
difference = sum_second_last - numbers[0]
product_fifth_sixth = numbers[4] * numbers[5]

var1 = sum_second_last
var2 = difference
var3 = product_fifth_sixth

print("Sum of second and last element:", var1)
print("Difference between previous result and first element:", var2)
print("Product of fifth and sixth elements:", var3)

# 3.

listn = ["good", "is", "programming"]

sentence_pos = listn[2] + " " + listn[1] + " " + listn[0]
print("Sentence (Positive Indices):", sentence_pos)

sentence_neg = listn[-1] + " " + listn[-2] + " " + listn[-3]
print("Sentence (Negative Indices):", sentence_neg)

# 4.

my_list = ['red', 'green', 'blue', 'yellow', 'purple']
print("Original List:", my_list)

my_list[2] = 'cyan'
my_list[3] = 'magenta'

print("Modified List:", my_list)