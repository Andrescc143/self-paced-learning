def palindrome(string):
    assert len(string) > 0, "You need to enter a non-empty string only"
    return string == string[::-1]

def run():
    user_entry = input("Type a string to evaluate if it is a palindrome: ")
    print(f"The result is: {palindrome(user_entry)}")

if __name__ == '__main__':
    run()