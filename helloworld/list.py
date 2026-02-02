letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
matrix = [[1, 2], [3, 4]]
zeros = [0] * 100
combined = letters + zeros
# print(combined)


numbers = list(range(20))
# print(numbers)
print(numbers[::-1])


# chars = list("Hello World")
# print(chars)


# unpacking
number = [1, 2, 3]
# first = number[0]
# second = number[1]
# third = number[2]
first, second, third = number
print(first, second, third)


numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first, second, rest)
