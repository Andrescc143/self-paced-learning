def make_division_by(n):
    """Function to create a division.

    Args:
        n (integer): Number to use as divisor
    Output:
        Function which receive a number to use a dividend, and returns the result of operate the dividen by the divisor.
    """
    def dividend(x):
        return x // n
    return dividend


def run():
    try:
        divisor = int(input('Enter the number you want to use as divisor: '))
        division = make_division_by(divisor)
        dividend = int(input('Enter the number you want to dividend: '))
        print(f'\n\nResult: {dividend} / {divisor} = {division(dividend)}')
    except ValueError:
        print('You need to type integers only. Try again')
        return False


if __name__ == '__main__':
    run()