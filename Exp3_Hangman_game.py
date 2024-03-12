import random

def choose_random_word():
    word_list = ["python", "hangman", "programming", "computer", "algorithm", "developer", "game"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_game():
    print("Welcome to Hangman Game!")
    player_name = input("Enter your name: ")
    selected_word = choose_random_word()
    max_attempts = 6
    guessed_letters = []
    attempts_left = max_attempts

    print(f"\nHello {player_name}! Try to guess the word.")

    while attempts_left > 0:
        current_display = display_word(selected_word, guessed_letters)
        print(f"\nWord: {current_display}")
        guess = input("Enter your guess (a single letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in selected_word:
            attempts_left -= 1
            print(f"Incorrect! Attempts left: {attempts_left}")
        else:
            print("Correct!")

        if set(guessed_letters) >= set(selected_word):
            print("\nCongratulations! You guessed the word:", selected_word)
            break

    if attempts_left == 0:
        print("\nGame over! You ran out of attempts. The correct word was:", selected_word)

# Main program
hangman_game()
