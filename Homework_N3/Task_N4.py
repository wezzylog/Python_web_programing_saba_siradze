#Using random library to initialize numbers duplication
import random

numbers = [random.randint(1, 4) for _ in range(5)]
print("Original -", numbers)
#creating a new_list and duplicating numbers
new_list = []
for n in numbers:
    for _ in range(n):
        new_list.append(n)
#prints out list and its length
print("List -", new_list)
print("Length -", len(new_list))