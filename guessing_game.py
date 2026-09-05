import random

number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")
        break