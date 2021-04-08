'''
fibonacci.py

Script containing functions fibonacci(n) and fast_fibonacci(), a recursive
fibonacci caluclator and a faster implementation. Calculates n-th position
in fibonacci sequence and times the calculation.

@author Alec Parfitt

'''

import time

def fibonacci(n):
    if n == 0:
        return 0
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) 

def fast_fibonacci(n):
    if n == 0:
        return 0
    if n < 2:
        return 1
    last = 1
    current = 1
    while (n > 2):
        n -= 1
        next = last + current
        last = current
        current = next
    return current

if __name__ == '__main__':
    
    n = int(input('Enter n for fibonacci(n): '))

    fib_type = input('Enter f for regular fibonacci, enter ff for fast fibonacci, enter q to quit:\n')
    while fib_type != 'q':
        if fib_type == 'f':
            timer = time.time()
            print(f'\nRecursive fibonacci of n: {fibonacci(n)}\n')
            print(f'Calculated in {time.time() - timer:.3f} seconds')
        elif fib_type == 'ff':
            timer = time.time()
            print(f'\nFast fibonacci of n: {fast_fibonacci(n)}\n')
            print(f'Calculated in {time.time() - timer:.3f} seconds')
        n = int(input('Enter n for fibonacci(n): '))
        fib_type = input('Enter f for regular fibonacci, enter ff for fast fibonacci, enter q to quit:\n')
        