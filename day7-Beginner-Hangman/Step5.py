import random
import hangman_words
#Step 5
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["aardvark", "baboon", "camel"]
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Create blanks
display = ["_"for i in range(len(chosen_word))]
print(" ".join(display))
end_of_game = False
while not end_of_game:
    guess = input("guess a letter:").lower()

    #Check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if not guess in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(" ".join(display))
    print(stages[lives])
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win")
    