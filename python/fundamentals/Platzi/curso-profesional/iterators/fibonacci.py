# Code to create an iterator which return the Fibonacci series
import time


class FiboIter:
    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.num1
        elif self.counter == 1:
            self.counter += 1
            return self.num2
        else:
            self.aux = self.num1 + self.num2
            self.num1, self.num2 = self.num2, self.aux
            self.counter += 1
            return self.aux


def run():
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1)
        

if __name__ == '__main__':
    run()