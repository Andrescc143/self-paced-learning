from math import sqrt

def run():
    dictionary = {i:sqrt(i) for i in range(1, 1001)}
    print(dictionary)

if __name__ == '__main__':
    run()