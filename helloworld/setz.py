# collection with no duplicate items
numbers = {1, 2, 3, 4, 5, 1, 2}
unique_numbers = set(numbers)
print(unique_numbers)

first_set = {1, 2, 3}
second_set = {3, 4, 5}

print(first_set | second_set)  # Union
print(first_set & second_set)  # Intersection
print(first_set - second_set)  # Difference
print(first_set ^ second_set)  # Symmetric Difference
