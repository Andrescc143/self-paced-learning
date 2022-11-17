import os


def get_words(dir):
    try:
        with open(dir, 'r', encoding='utf-8') as f:
            return [word for word in f.read().splitlines()]
             
    except:
        print('Error when trying to open the file with the words to use for the game.')
        return False

def find_letter(letter, word):
    return [i for i, letr in enumerate(word) if letr == letter]
        

def start_game(word):
    guessed = {}
    unique_letters = set(word)
    tries = 0
    
    while len(guessed) < len(unique_letters):
        tries += 1
        os.system('cls')
        progress = ''
        for letter in word:
            if guessed.get(letter):
                progress += letter + ' '
            else:
                progress += '-' + ' ' 
        print("That's how you go: ", progress)
        print(f'Guessed: {len(guessed)}. Total letters: {len(word)}')
        new_letter = input('Enter the letter you want to try: ')
        searching_result = find_letter(new_letter, word)
        
        if len(searching_result) != 0:
            guessed[new_letter] = searching_result
        else:
            input('Ups, wrong choice...\n\nReady to try again? Press a key to continue')
        os.system('cls')
        print(f'YOU WIN !!!\nWord: {word}  Total tries: {tries}')
             

def run():
    while True:
        os.system("cls")
        welcome_message = """***** HANGMAN *****\nReady to play? y/n\n"""
        start_command = input(welcome_message)
        
        if start_command in ('y', 'Y'):
            words = get_words('./data.txt')
            word_index = int(input(f'Select a number between 0 and {len(words)}: '))
            word_to_play = words[word_index]
            start_game(word_to_play)     
        else:
            break
          
        restart_command = input('\n\nGAME OVER\nWanna play again? y/n\n')
        if restart_command in ('y', 'Y'):
            continue
        else:
            print('What a little girl... see you.')
            break

if __name__ == '__main__':
    run()