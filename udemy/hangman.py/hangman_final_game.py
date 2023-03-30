
import random
import hangman_alphabet
from hangman_words_list import word_list
from hangman_art import stages
from hangman_art import logo


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game: 
    valid_guess = False
    while not valid_guess:
        guess = input("Guess a letter: \n").lower()
        if guess not in hangman_alphabet.alphabet:
            print("That is not a valid answer. Please guess one letter.\n")
        else:
            valid_guess = True
            
    if guess in guessed_letters:
        print(f"You have already guessed {guess}\n")
        continue
    guessed_letters += guess
    

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
            print(f"{guess} is not a letter in the word. You lose a life.\n")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You Lose\n")
                print(f"The word was {chosen_word}\n")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nYOU WIN!")

    print(stages[lives])