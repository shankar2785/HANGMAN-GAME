import random

def choose_randomeword():
    words = ["hangman", "python", "code", "learning", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_player_input():
    return input("Guess a letter: ").lower()

def hangman_game():
    selected_word = choose_randomeword()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    incorrect_guess_list = []

    while True:
        display = display_word(selected_word, guessed_letters)
        print("Current word:", display)
        print("Incorrect guesses:", incorrect_guess_list)

        if display == selected_word:
            print("Congratulations! You guessed the word:", selected_word)
            break

        if incorrect_guesses == max_incorrect_guesses:
            print("Sorry, you ran out of guesses. The word was:", selected_word)
            break

        player_guess = get_player_input()

        if len(player_guess) == 1:
            if player_guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif player_guess in selected_word:
                guessed_letters.append(player_guess)
                print("Good guess!")
            else:
                incorrect_guesses += 1
                incorrect_guess_list.append(player_guess)
                print("Incorrect guess. Remaining attempts:", max_incorrect_guesses - incorrect_guesses)
        elif len(player_guess) == len(selected_word) and player_guess.isalpha():
            if player_guess == selected_word:
                print("Congratulations! You guessed the word:", selected_word)
                break
            else:
                incorrect_guesses += 1
                incorrect_guess_list.append(player_guess)
                print("Incorrect guess. Remaining attempts:", max_incorrect_guesses - incorrect_guesses)
        else:
            print("Invalid input. Please enter a single letter or the entire word.")


hangman_game()
