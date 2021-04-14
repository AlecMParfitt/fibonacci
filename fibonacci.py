'''
fibonacci.py

requires matplotlib
requires numpy

Script containing functions fibonacci(n) and fast_fibonacci(n), a recursive
fibonacci caluclator and a faster implementation. Calculates n-th position
in fibonacci sequence and times the calculation. Graphing shows time to calculate
similar n-th position

@author Alec Parfitt

'''

import time
from matplotlib import pyplot as plt

def fibonacci(n):
    """Recursive Fibinacci calculation

    Args:
        n (int): n-th position in Fibonacci sequence to retrieve

    Returns:
        int: n-th position in fibonacci sequence
    """
    if n == 0:
        return 0
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) 

def fast_fibonacci(n):
    """Fast, non-recursive implementation of fibonacci calculator

    Args:
        n (int): n-th position of fibonacci sequence to be found

    Returns:
        int: n-th position in fibonacci sequence
    """
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

def generate_timed_plot():
    """Generate plot does not accept n values as plots could end up
       never being generated
    """
    full_timer = time.time()
    plt.ylabel('sec to calculate')
    plt.xlabel('n position in fib sequence')
    plt.title('Time to find n-th position in Fib sequence')
    x = []
    y = []
    for i in range(34):
        timer = time.time()
        fibonacci(i)
        timer = time.time() - timer
        x.append(i)
        y.append(timer)
    plt.plot(x,y)
    
    x2 = []
    y2 = []
    for j in range(45):
        timer = time.time()
        fast_fibonacci(j)
        timer = time.time() - timer
        x2.append(j)
        y2.append(timer)
    plt.plot(x2,y2)
    full_timer = time.time() - full_timer
    print(f'done in {full_timer:.0f} seconds!\n')

def print_menu():
    print('\nSelect an option below or q to quit')
    print()
    print('      set - set new n position')
    print('        f - recursive fib')
    print('       ff - fast fib')
    print('      gen - generate graphs (this may take a while)')
    print('       sh - show graphs')
    print('        q - quit')
    print('_________________________________________')
    
if __name__ == '__main__':
    n = 25
    print_menu()
    selection = input('>>| ')
    print('_________________________________________')
    while selection != 'q':
        print(f'current n: {n}')
        if selection == 'f':
            timer = time.time()
            print(f'\nRecursive fibonacci of n: {fibonacci(n)}\n')
            print(f'Calculated in {time.time() - timer:.3f} seconds')
            print('_________________________________________')
        elif selection == 'ff':
            timer = time.time()
            print(f'\nFast fibonacci of n: {fast_fibonacci(n)}\n')
            print(f'Calculated in {time.time() - timer:.3f} seconds')
            print('_________________________________________')
        elif selection == 'gen':
            generate_timed_plot()
        elif selection == 'sh':
            plt.show()
        elif selection == 'set':
            n = int(input('Enter new n number: '))
        print_menu()
        selection = input('\n>>| ')
        print('_________________________________________')
        