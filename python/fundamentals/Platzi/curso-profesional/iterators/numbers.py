#Code to make an iterable which shows all the positive integers
import time


class NumberIter:
    def __init__(self, max=None):
        self.max = max
        
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 1
            return result
        else:
            print('Maximum number reached')
            raise StopIteration


def run():
    num_iterable = NumberIter()
    for element in num_iterable:
        print(element)
        time.sleep(1)
        

if __name__ == '__main__':
    run()