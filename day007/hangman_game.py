import os
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

# set lives equal to six
lives = 6

# randomly chosen word
chosen_word = random.choice(word_list)

# shoud add an underscore for each letter in chosen word
display = []

for letter in chosen_word:
    display += '_'

end_of_game = False

while not end_of_game:
    # ask for user input
    guess = input('Guess a letter: ').lower()

    os.system('cls' if os.name == 'nt' else 'clear')

    if guess in display:
        print(f"You've already guessed {guess} ")

    # check if the user input is one of the words in the list
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1

        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            end_of_game = True
            print('You lose')

    print(f'{ " ".join(display)}')

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])
