import random

print("Welcome to number guessing game.\n")
right_number = random.randint(1, 100)

print("I've picked a number for you to guess.")
print("The number is between 1 and 100.\n")

guessed_number = int(input("Guess a number: "))

while guessed_number != right_number:
    if guessed_number < 1 or guessed_number > 5:
        print("Invalid guess. Please enter a number between 1 and 5.")

    elif guessed_number > right_number:
        print("\nYour guess is not correct.")
        print("Give it another shot.")
        print("Choose a lower number.\n")
    else:
        print("\nYour guess is not correct.")
        print("Give it another shot.")
        print("Choose a higher number.\n")

    guessed_number = int(input("Enter guess number again: "))
print("\nCorrect guess 👍.")
print("You won. Thank you for playing.⭐⭐⭐")