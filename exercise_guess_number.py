import random

number = random.randint(0, 10)
while True:
    try:
        guess = int(input("Guess a number (0-10): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            break
    except ValueError:
        print("Invalid, please enter only numbers")