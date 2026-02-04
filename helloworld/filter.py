items = [
    ("Product A", 29.99),
    ("Product B", 49.99),
    ("Product C", 19.99),
]

filtered_items = list(filter(lambda item: item[1] > 30, items))
print(filtered_items)
