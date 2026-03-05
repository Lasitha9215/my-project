import random

number = random.randint(1, 20) 
guess = 0
attempts=0

print("Guess a number between 1 and 20")

while guess != number:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"You guessed it correct! The number was {number}. Attempts: {attempts}")