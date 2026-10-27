import random

# ASCII Gallows Art stages corresponding to remaining attempts (6 down to 0)
STAGES = [
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,  # 0 attempts left (Defeat)
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,  # 1 attempt left
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,  # 2 attempts left
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,  # 3 attempts left
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,  # 4 attempts left
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,  # 5 attempts left
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """   # 6 attempts left (Initial state)
]

# Fallback word list if an external words list file is not present
DEFAULT_WORDS = [
    "PYTHON", "DEVELOPkER", "HANGMAN", "PROGRAMMING",
    "ALGORITHM", "COMPUTER", "SOFTWARE", "TERMINAL",
    "VARIABLE", "FUNCTION", "KEYBOARD", "DATABASE"
]

def load_words(file_path="words.txt"):
    """Loads word list from a file or falls back to default list."""
    try:
        with open(file_path, "r") as file:
            words = [line.strip().upper() for line in file if line.strip().isalpha()]
            if words:
                return words
    except FileNotFoundError:
        pass
    return DEFAULT_WORDS

def get_masked_string(secret_word, guessed_letters):
    """Returns the secret word masked with underscores for un-guessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def play_game():
    """Runs a single round of the Hangman game."""
    words = load_words()
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6

    print("=======================================")
    print("      WELCOME TO HANGMAN GAME!         ")
    print("=======================================")

    while len(incorrect_guesses) < max_attempts:
        attempts_left = max_attempts - len(incorrect_guesses)
        
        # Display current visual stage, masked word, and guessed letters
        print(STAGES[attempts_left])
        print(f"Word: {get_masked_string(secret_word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining Attempts: {attempts_left}\n")

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("=======================================")
            print(" 🎉 VICTORY! YOU GUESSED THE WORD! 🎉 ")
            print(f" Word: {secret_word}")
            print("=======================================")
            return

        # Prompt for user input
        guess = input("Guess a letter: ").strip().upper()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️ Invalid input! Please enter a single alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print(f"\n⚠️ You already guessed '{guess}'. No penalty deduction.\n")
            continue

        # Process guess
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"\n✅ Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses.add(guess)
            print(f"\n❌ Wrong guess! '{guess}' is not in the word.\n")

    # Defeat condition
    print(STAGES[0])
    print("=======================================")
    print(" 💀 GAME OVER! YOU RAN OUT OF ATTEMPTS. 💀")
    print(f" The secret word was: {secret_word}")
    print("=======================================")

def main():
    """Main loop allowing the user to play multiple rounds."""
    while True:
        play_game()
        replay = input("\nWould you like to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()