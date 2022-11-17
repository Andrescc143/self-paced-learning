# Code to show the advantages of decorators
from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kargs):
        initial_time = datetime.now()
        result = func(*args, **kargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Execution time: {time_elapsed.total_seconds()}')
        return result
    return wrapper


@execution_time
def suma(a: int, b: int) -> int:
    return a + b

def run():
    print(f'The result of add 8 plus 10 is: {suma(8, 10)}')

if __name__ == '__main__':
    run()
