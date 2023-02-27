from balansed import is_balanced
from stack import Stack
from mail import Mailer
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    
    print('****'*20)
    print('BALANS:')
    blns_data = input('Введите последовательность, для проверки сбалансированности: ')
    print(is_balanced(blns_data))
    print('****'*20)
    
    print('STACK:')
    a = [1, 2, 3, 4, 5]
    stack = Stack(a)
    stack2 = Stack(a)

    print(stack)
    print(f'STACK SIZE = {stack.size()}')
    print(f'STACK IS EMPTY - {stack.is_empty()}')
    stack.pop()
    for element in stack:
        print(element)