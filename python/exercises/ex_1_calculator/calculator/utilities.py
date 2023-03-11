def num_to_operate():
    numbers = input("Type the numbers you want to operate separated by a blanck space: ")
    
    try:
        num_to_operate = list(map(lambda x: int(x), numbers.split()))
    except:
        print("Check the values entered, they must be all numbers !\n")
        return False
    
    return num_to_operate