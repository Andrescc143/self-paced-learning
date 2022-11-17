# Code to evaluate whether a number is prime or not

def is_prime(number: int) -> bool:
    """
    Function to evaluate if a number is prime or not.
    Input: Integer
    Output: Boolean
    """
    divisors = [x for x in range(1, number + 1) if number % x == 0]
    return [1, number] == divisors

def run():
    print(f'Is the {'80'} a prime number?\n--> {is_prime('80')}')


if __name__ == '__main__':
    run()