"""
Code to evaluate whether a word is a palindrome or not
"""

def palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


def run():
    word = 8000
    print(f'Is the word {word} a Palindrome?\n--> {palindrome(word)}')


if __name__ == '__main__':
    run()