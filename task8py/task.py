from random import randint
from math import pow

def num(length):
    numbers = [randint(20, 50) for _ in range(length)]
    numbers = [(pow(num, 2)) if num % 2 == 0 else num for num in numbers]
    return numbers
print(num(5))