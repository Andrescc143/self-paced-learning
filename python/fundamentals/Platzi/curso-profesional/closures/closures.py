# Code to create a Closure

def timeStr(string):
    """Function to create a Closure. It creates a function which remembers the string entered by the user, and return the nested function.

    Args:
        string (str): string to print multiple times.
    Output:
        multiplier (func): Function which remember the string entered and receive a value n to use as multiplier to print the string n times
    """
    
    assert not string.isnumeric(), 'You must enter strings only'
    def multiplier(n):
        return f'{string} ' * n
    
    return multiplier

def run():
    word_to_print = input('Enter the word you want to print multiple times: ')
    timesWord = timeStr(word_to_print)
    
    try:
        times = int(input('How many times you want me to print the word?: '))
        print(timesWord(times))
    except ValueError:
        print('You must enter integers only. Try again')

if __name__ == '__main__':
    run()