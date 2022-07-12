# Hang man Game ////
import random

from words import words


import string


def get_valiad_word(words): 

    word = random.choice(words)

    while '_' in word or ' ' in word :

        word = random.choice(words)

    return word.upper()

while True :
    def hangman() : 

        word = get_valiad_word(words)
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        lives = 10

        while len(word_letters) > 0 and lives > 0:

            # ''.join used to turn ['a' , 'b' , 'c'] to ==> a b c
            print('The letters that you have used : ', ''.join(used_letters),'\n')

            # What letter is lift (ex  :  W _ R D)
            word_list = [letter if letter in used_letters else '_' for letter in word]
            print('Current word : ', ' '.join(word_list))
            print(f'You Have {lives} Chances ')
            user_letter = input('\nEnter a litterr to guess the word : ').upper()

            if user_letter in alphabet - used_letters :

                used_letters.add(user_letter)

                if user_letter in word_letters : 

                    word_letters.remove(user_letter)
                else : 
                    lives -= 1
                    print(f'letter {user_letter} is not in the word')
            elif user_letter in user_letter : 

                print('You had jast used that letter , please try again  ')

            else : 

                print('Invalid character just try again')


        if lives == 0 :

            print(f'RIP, The word was {word}')

        else : 

            print(f'Congrats you guessed the word {word} the guy will be exempted')

    choice = input('Wanna play  : (Y/N)?').upper()
    if choice == 'Y' or choice == 'YES' :

        hangman()
    else :
        break
