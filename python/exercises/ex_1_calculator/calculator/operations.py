from functools import reduce

def addition(*args):
    return reduce((lambda a, b: a + b), args)

def subtraction(*args):
    return reduce((lambda a, b: a - b), args)

def division(*args):
    return reduce((lambda a, b: a / b), args)

def multiplication(*args):
    return reduce((lambda a, b: a * b), args)