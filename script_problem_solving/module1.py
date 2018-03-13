"""Main"""
from module1_2 import *

a = 0
while True:
    print(eggs.spam)
    if a:
        from module2 import bar
        print(bar())
    choice = input()
    if choice == '0':
        break
    elif choice == '1':
        a = 1
    elif choice:
        eggs.spam = choice
