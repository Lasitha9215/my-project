import random

number = random.randint(1, 30) 
guess = 0

print("Guess a number between 1 and 30")

while guess != number:
    guess = int(input("Your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("You guessed it! The number was", number)