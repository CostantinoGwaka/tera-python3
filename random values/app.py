import random
import string

print(random.random())  # Random float:  0.0 <= x < 1.0
print(random.randint(1, 10))  # Random integer: 1 <= x <= 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random element
print(random.choices([1, 2, 3, 4], k=2))  # Random element
# Random sample of 5 unique numbers from 1 to 99
print(random.sample(range(1, 100), 5))
print(random.shuffle([1, 2, 3, 4, 5]))

print("".join(random.choices(string.ascii_letters + string.digits, k=10)))
# print(string.ascii_letters)
