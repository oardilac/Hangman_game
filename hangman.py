#Import the files and libraries that will be used
import random
import os #to clear screen
from data import EN_WORDS
from variables import *

def read_data() -> str: #returns a word from data file
    words = []
    for line in EN_WORDS:
        words.append(line.strip().upper())
    return words

def run():
    data = read_data()
    chosen_word: str = random.choice(data)
    chosen_word_list: str = [letter for letter in chosen_word]
    chosen_word_list_underscores: str = ["_"] * len(chosen_word_list) #saves the lenght of the word in underscores
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
      
    
    lifes = 7 #Takes the stages of the hangaman to print them later

    while True:
        os.system("cls") #clears the terminal
        print("Remember: You have " + str(lifes) +" lifes. Be careful")
        print(STATEGES) 

        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")


        try:
            letter = input("Enter a letter and press Enter: ").strip().upper()
            assert letter.isalpha(), input("YOU CAN ONLY ENTER LETTERS!, Press the key Enter to continuous")
            assert len(letter) == 1, input("ONLY A LETTER, PLEASE!, Presss the key Enter to continous")
        except AssertionError as e:
            print(e)
            continue    


        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            lifes -= 1
            if lifes == -1:
                os.system("cls") #clears the terminal

                lose = input(LOST).upper()
                if lose == "X":
                    lifes = 7
                    chosen_word = random.choice(data)
                    chosen_word_list = [letter for letter in chosen_word]
                    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
                    letter_index_dict = {}
                    for idx, letter in enumerate(chosen_word):
                        if not letter_index_dict.get(letter): 
                            letter_index_dict[letter] = []
                        letter_index_dict[letter].append(idx)
                    continue
                else:
                    break



        if "_" not in chosen_word_list_underscores:
            os.system("cls") #clears the terminal
            print(WIN)
            print("Congratulations! You made it. The word was: ", chosen_word)
            choice = input("Press the key (X) to play again or press any other key to left\n").upper()
            if choice.upper() == "X":
                lifes = 7
                chosen_word = random.choice(data)
                chosen_word_list = [letter for letter in chosen_word]
                chosen_word_list_underscores = ["_"] * len(chosen_word_list)
                letter_index_dict = {}
                for idx, letter in enumerate(chosen_word):
                    if not letter_index_dict.get(letter): 
                        letter_index_dict[letter] = []
                    letter_index_dict[letter].append(idx)
                continue
            else:
                break


menu = HANGMAN_TITLE #Output printed by console and show the first screen


while True:
    try:
        opcion = input(menu)
        if int(opcion) == 1:
            run()   
        else: input("You have to enter the number 1 to play. Press the key Enter to retry")
        assert len(str(opcion)) == 1, input("You don't have to enter several words or numbers!, Press the key Enter to retry")
    except AssertionError as a:
        print(a) 
    except ValueError:
        input("Don't accept letters, enter the number 1 to play. Press the key Enter to retry")   


if __name__ == '__main__':
    run()