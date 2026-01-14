import random

words = ["python", "coding", "intern", "alpha", "program"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Good guess!")
    else:
        attempts -= 1
        print(" Wrong guess! Attempts left:", attempts)

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

if attempts == 0:
    print("\n💀 Game Over! The word was:", secret_word)

