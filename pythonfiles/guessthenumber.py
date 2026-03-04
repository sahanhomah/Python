import random
number = random.randint(1, 100)
guess = int(input("Enter a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Enter a number between 1 and 100: "))

print("You guessed it!")