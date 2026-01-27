def printUserName(username):
    print(f"Hello, {username}!")


printUserName("Alice")


def increment(number: int = 1, by: int = 1):
    return (number, number + by)


print(increment(number=5, by=2))


def multiply(*list):
    total = 1
    for num in list:
        total *= num
    return total


print(multiply(1, 2, 3, 4, 5))


def save_user(**user):
    print(user["id"])


save_user(id=1, name="Alice", age=30)

message = "a"


def greet():
    # global message
    message = "b"
    print(message)


greet()
print(message)
