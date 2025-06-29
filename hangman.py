import random

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Normal")
    print("3. Difficult")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 'easy', 10
        elif choice == '2':
            return 'normal', 7
        elif choice == '3':
            return 'difficult', 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_word_by_difficulty(difficulty):
    easy_words = ['cat', 'dog', 'sun', 'hat', 'fish', 'book']
    normal_words = ['apple', 'house', 'robot', 'magic', 'ocean', 'green']
    difficult_words = ['elephant', 'computer', 'hangman', 'difficult', 'notebook', 'platform']

    if difficulty == 'easy':
        return random.choice(easy_words)
    elif difficulty == 'normal':
        return random.choice(normal_words)
    else:  # difficult
        return random.choice(difficult_words)

def hangman():
    difficulty, max_incorrect = choose_difficulty()
    word = get_word_by_difficulty(difficulty)
    guessed_letters = set()
    incorrect_guesses = 0

    print(f"\nWelcome to Hangman - {difficulty.upper()} mode!")
    print(f"The word has {len(word)} letters.")

    while True:
        # Display word with guessed letters
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord: " + ' '.join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry! '{guess}' is NOT in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            break

        if incorrect_guesses >= max_incorrect:
            print(f"\n💀 Game Over! The word was: {word}")
            break

if __name__ == "__main__":
    hangman()
