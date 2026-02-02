letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
items = (0, "a")
index, letter = items
print(index, letter)
for index, letter in enumerate(letters):
    print(index, letter)
