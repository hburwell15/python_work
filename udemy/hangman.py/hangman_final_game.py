#Step 5

import random
from hangman_words_list import word_list
from hangman_art import stages
from hangman_art import logo

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letters = []

while not end_of_game: 
    #TODO - If the user inputs more than one letter or a number, let them know and have them try again.
    valid_guess = False
    while not valid_guess:
        guess = input("Guess a letter: \n").lower()
        if len(guess) > 1:
            print("That is not a valid input. Please try again.")
        elif len(guess) == 1:
            valid_guess = True
            
        
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print(f"You have already guessed {guess}")
    guessed_letters += guess

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in a letter in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])