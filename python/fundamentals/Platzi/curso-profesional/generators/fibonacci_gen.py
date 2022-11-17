# Code to implement the Fibonacci series using generators
import time


def fibonacci_gen(max=None):
    num1 = 0
    num2 = 1
    counter = 0
    result = 0
    
    while not max or result <= max:  
        if counter == 0:
            counter += 1
            yield num1
        elif counter == 1:
            counter += 1
            yield num2
        else:
            counter += 1
            result = num1 + num2
            num1, num2 = num2, result
            yield result
        
    

def run():
    a = fibonacci_gen(30)
    try:
        while True:
            print(next(a))
            time.sleep(1)
    except StopIteration:
        print("Result is equal to or greater than the maximum value configured")

if __name__ == '__main__':
    run()
    