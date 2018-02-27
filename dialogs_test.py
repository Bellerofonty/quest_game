import sys
import json

def dump_data():
    dict1 = {'begin': ['Merchant', 'Hello, stranger', 'fork1'],
    'fork1': ['Merchant', 'Need something?', ['fork1-1', 'fork1-2', 'fork1-3']],
    'fork1-1':['Player', 'Let\'s trade', 'trade'],
    'fork1-2':['Player', 'Need some repairs', 'repairs'],
    'fork1-3':['Player', 'May be, later', 'goodbye'],
    'trade': ['code', 'trade()', 'fork1'],
    'repairs': ['code', 'repairs()', 'fork1'],
    'goodbye': ['Merchant', 'Come again', 'end'],
    'end': ['code', 'sys.exit()', 'fork1']}

    with open('dialogs/new_dialog.txt', "w", encoding="utf-8") as file:
        json.dump(dict1, file)

def trade():
    print('trading')

def repairs():
    print('repairing')

dump_data()

with open('dialogs/new_dialog.txt', "r", encoding="utf-8") as file:
    dialog = json.load(file)

##print(dialog['begin'][2])
##print(type(dialog['begin'][2]))
##print(dialog[dialog['fork1'][2][1]][2])

phrase_code = 'begin'
while True:
    phrase = dialog[phrase_code]
    if phrase[0] == 'code':
##        print(phrase[1])
        exec(phrase[1])
    else:
        print('--{}--\n{}'.format(phrase[0], phrase[1]))

    if type(phrase[2]) is str:
        phrase_code = phrase[2]
    else:
        input()
        print('')
        fork = phrase[2]
        print('--{}--'.format(dialog[fork[0]][0]))
        for num, i in enumerate(fork):
            print(num + 1, dialog[i][1])
    choice = input()
    try:
        choice = int(choice)
    except ValueError:
        pass
    if choice == 0:
            sys.exit()
    if choice:
        phrase_code = dialog[phrase[2][choice - 1]][2]
    print('')

