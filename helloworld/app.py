x = 1
y = 2
unit_price = 3


student_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
multiple = '''
haha
code
gwaka
'''

x = 1
y = 2
x, y = 1, 2
x = y = 1

data_value = 29
# print(type(data_value))


integer_value: int = 10


print(type(integer_value))


name = "John Doe"
len(name)
print(len(name))

name[0]
print(name[0])
print(name[-1])
print(name[0:4])  # slicing
print(name[:4])  # slicing
print(name[::2])  # skipping
print(name[0:])
print(name[:])

print(id(name))
print(id(name[0]))

name_here = "Jane \"Doe"
# \' \\ \n \t \"
print(name_here)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
full_name2 = f"{first_name} {last_name}"
print(full_name2)

course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("Pro", "-"))

print("Progammin" in course)
print("Progammin" not in course)


# number
x = 10
x = 0b10
print(x)
print(bin(x))

x = 0x12c
print(x)
print(hex(x))

# complex number
x = 3 + 5j
print(x)

# arthmetic operators
x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3
print(x)
x = 10 // 3
print(x)
x = 10 % 3
print(x)
x = 10 ** 3
print(x)


# CONSTANTS

PI = 3.14
print(round(PI))
print(abs(PI))

# type conversion int(x), float(x), str(x), bool(x)
# bool falsy values: 0, 0.0, "", None, [], {}, set()
# x = input("Enter a number: ")
# x = int(x) + 1
print(x)

print(bool(0))


# conditional statements
age = 13
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a minor.")

print("End of program.")

# logical operators: and, or, not
name = "Gwaka"

if not name.strip():
    print("Name is empty.")
else:
    print("Name is not empty.")

age = 2
if age >= 18 and name == "Gwaka":
    print("Adult Gwaka.")

# ternary operator
message = "Costantino Gwaka" if age >= 18 else "Minor Gwaka"
print(message)


# foor loop
# for i in range(5):
#     print(i)

for i in range(0, 10, 2):
    print(i)

# for x in "Gwaka":
#     print(x)

# for item in ["apple", "banana", "cherry"]:
#     print(item)


print(type(range(5)))
print([1, 2, 3, 4, 5, 6, 7, 8, 9])

names = ["Alice", "Kob", "Charlie"]
for name in names:
    if name.startswith("B"):
        print("Found a name starting with B:", name)
        break
else:
    print("No name starting with B found.")
