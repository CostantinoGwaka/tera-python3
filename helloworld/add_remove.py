letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# ADD
letters.append("k")
letters.insert(0, "z")
print(letters)


# REMOVE
letters.pop()
letters.remove("c")
del letters[0]
letters.clear()
print(letters)
