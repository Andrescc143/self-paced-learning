"""
Script para encontrar los números primos entre 1 y 101 y visualizarlos en pantalla
"""

def is_prime(x):
    if x < 2:
        print(f"El número {x} no es un número válido a evaluar")
        return False
    else:
        for number in range(2, x):
            if x % number == 0:
                return False
        return True

primes = [number for number in range(1, 101) if is_prime(number)]
print(primes)
