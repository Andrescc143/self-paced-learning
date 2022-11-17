def read():
    with open('./numbers.txt', 'r', encoding='utf-8') as f:
        numbers = [int(number) for number in f]
    return numbers
        

def write():
    names = ['Camilo', 'Andrés', 'Palencia', 'Castañeda']
    with open('./names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    print(write())

if __name__ == '__main__':
    run()