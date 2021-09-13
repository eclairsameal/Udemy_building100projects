import random
import hangman_words
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
import hangman_art
#Step 5
stages = hangman_art.stages
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["aardvark", "baboon", "camel"]
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
lives = 6
#Create blanks
display = ["_"for i in range(len(chosen_word))]
print(" ".join(display))
end_of_game = False
while not end_of_game:
    guess = input("guess a letter:").lower()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in chosen_word:
        end_of_game = True
        print("You've already guessed {}.".format(guess))
    #Check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if not guess in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print("You guessed {},.that's not in the word. You lose a life.".format(guess))
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")

    print(" ".join(display))
    
    print(stages[lives])
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win")
    