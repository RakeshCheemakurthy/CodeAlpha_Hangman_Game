import random

print("Welcome to Hangman Game")

words = ["python", "code", "game", "alpha", "chat"]
word = random.choice(words)

guessed = []
wrong = 0

while wrong < 6:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print("Word:", display)

    if "_" not in display:
        print("You Win")
        break

    guess = input("Enter letter: ")
    if guess in word:
        guessed.append(guess)
        print("Correct")
    else:
        wrong += 1
        print("Wrong Remaining:", 6 - wrong)

if wrong == 6:
    print("Game Over Word was:", word)
