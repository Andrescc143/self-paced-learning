def divisors(num):
    return [x for x in range(1, num+1) if num % x == 0]

def run():
    try:
        user_input = int(input("Ingresa un número: "))
        if user_input < 0:
            raise ValueError
            return False
        print(divisors(user_input))
    except ValueError:
        print("You need to enter positive numbers only.")
        return False


if __name__ == '__main__':
    run()