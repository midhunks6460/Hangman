import random

def choose_word():
    # List of words for the game
    words = ['python', 'hangman', 'example', 'computer', 'programming', 'javascript']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    # Display the word with guessed letters and underscores for unguessed letters
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6  # Maximum allowed attempts

    while max_attempts > 0:
        print("\nAttempts left:", max_attempts)
        print("Guessed letters:", ' '.join(guessed_letters))
        print("Current word:", display_word(word_to_guess, guessed_letters))

        user_guess = input("Enter a letter or the whole word guess: ").lower()

        # Check if the user input is a valid single letter or a complete word guess
        if len(user_guess) == 1 and user_guess.isalpha():
            # Check if the letter has already been guessed
            if user_guess in guessed_letters:
                print("You already guessed that letter!")
            elif user_guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(user_guess)
            else:
                print("Wrong guess!")
                max_attempts -= 1
        elif len(user_guess) == len(word_to_guess) and user_guess.isalpha():
            # Check if the whole word guessed is correct
            if user_guess == word_to_guess:
                print("Congratulations! You guessed the word correctly: " + word_to_guess)
                return
            else:
                print("Wrong guess!")
                max_attempts -= 1
        else:
            print("Invalid input. Please enter a valid letter or the whole word guess.")

        # Check if the word has been guessed completely
        if display_word(word_to_guess, guessed_letters).replace(" ", "") == word_to_guess:
            print("Congratulations! You guessed the word correctly: " + word_to_guess)
            return

    print("Sorry, you ran out of attempts. The word was: " + word_to_guess)


if __name__ == "__main__":
    hangman()
