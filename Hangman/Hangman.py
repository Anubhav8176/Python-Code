import random
import Hangman_lib

# List of the words to be selected from
#word_list = ["aardvark", "baboon", "camel"]

print(Hangman_lib.logo)

# Choosing a random word from the list of words
chosen_word = random.choice(Hangman_lib.word_list)
life = len(chosen_word)

# Creating a blanklist that is used for replacing the correct answers
blank_list = []
for _ in range(len(chosen_word)):
    blank_list += "_"
print(blank_list)

# A variable that keep the track of lives user has left.
lives = 6

# Checking if the user guessed the word correct or wrong.
flag = False
print(f"The chosen word is {chosen_word}")
while not flag == True:
    guess = input("Guess a letter: ").lower()

    # Checking that the user already entered the correct guessed letter
    if guess in blank_list:
        print(f"You have already guessed the letter {guess} earlier")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            blank_list[position] = letter
    print(blank_list)

    # Checking if user has left any lives or not if not then end game i.e lives = 0
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed letter {guess} which is not in word, you lose a life.")
        if (lives == 0):
            print(f"You lose and you have {lives}")
            flag = True

    # Checking if there is any blank space in the blanklist or not if not then end game.
    if "_" not in blank_list:
        flag = True
        print("You won")

    # Printing the lives user had in their pocket.
    print(Hangman_lib.stages[lives])
