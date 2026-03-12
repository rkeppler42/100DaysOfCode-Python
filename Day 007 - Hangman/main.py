import random

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list


lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    if guess in guessed_letters:
        print(f"You already guessed this letter: {guess}")
    else:
        guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word" )

        if lives == 0:
            game_over = True

            print(f"The correct word was: {chosen_word}")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
