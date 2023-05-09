import random
#Import the words from hangman_words.py 
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Import the logo from hangman_display.py and print it at the start of the game.
from hangman_display import logo
print(logo)
# print(f' the solution is {chosen_word}.')
#Create blanks to start with
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()