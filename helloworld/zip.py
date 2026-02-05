list1 = [1, 2, 4]
list2 = [10, 20, 40]


# [(1, 10), (2, 20), (4, 40)]
zipped = zip(list1, list2)
print(list(zipped))
