guess = 0
answer = 5

while guess != answer:
    guess = int(input("Enter your guess (0-10): "))
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print("Correct! You've guessed the number.")
        break
