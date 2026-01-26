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
