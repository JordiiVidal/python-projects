import json
import random
from hangman.classes.Hangman import Hangman


def get_data(file):
    list_words = []
    json_file = open(file, 'r')
    if json_file.readable():
        data = json.load(json_file)
        for w in data['words']:
            list_words.append(w)
    return list_words


words = get_data('data.json')
word = random.choice(words)
hang_man = Hangman(word)

while not hang_man.win() and hang_man.lives > 0:
    print(f"Actual State :  {hang_man.state} ({len(hang_man.state)} Letters) with {hang_man.lives} lives")
    print("Commands (1): Show used letters")
    letter = input("Enter a letter? ")
    if letter == "1":
        print(hang_man.used_letters)
    elif len(letter) > 1:
        print("Please enter only one letter")
    elif letter not in hang_man.used_letters:
        hang_man.check_letter(letter)
    else:
        print("Used letter")


if hang_man.win():
    print(f" You Win {hang_man.state}")
else:
    print(f"Sorry you lose the game, the word was {hang_man.word}")

