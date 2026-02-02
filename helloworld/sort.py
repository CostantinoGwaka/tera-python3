numbers = [1, 2, 4, 3, 5]
numbers.sort(reverse=True)
print(numbers)
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)


# ORDER
items = [
    ("product1", 10),
    ("product2", 5),
    ("product3", 20),
]


def sort_item(item):
    return item[1]


# items.sort(key=sort_item, reverse=True)
# items.sort(key=lambda item: item[1], reverse=True) # descending order lambda function
items.sort(key=lambda item: item[1],)


print(items)
