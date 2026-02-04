items = [
    ("Hello, World!", "A classic programming example."),
    ("Python", "A popular programming language known for its readability."),
    ("Map", "A data structure that associates keys with values."),
]

print(list(map(lambda item: item[1], items)))

courseName = []
for items in items:
    courseName.append(items[1])

print(courseName)
