import sys
import json

##dict1 = {'begin': ['Merchant', 'Hello, stranger', 'fork1'],
##'fork1': ['Merchant', 'Need something?', ['fork1-1', 'fork1-2', 'fork1-3']],
##'fork1-1':['Player', 'Let\'s trade', 'trade'],
##'fork1-2':['Player', 'Need some repairs', 'repairs'],
##'fork1-3':['Player', 'May be, later', 'end'],
##'trade': ['code', 'trade()', 'begin'],
##'repairs': ['code', 'repairs()', 'begin'],
##'end': ['code', 'sys.exit()', 'begin']}
##print(dict1['begin'])
##with open('dialogs/new_dialog.txt', "w", encoding="utf-8") as file:
##    json.dump(dict1, file)

with open('dialogs/new_dialog.txt', "r", encoding="utf-8") as file:
    dialog = json.load(file)
##    print(dialog['begin'])

##print(dialog['begin'][2])
phrase_code = 'begin'
##print(type(dialog['begin'][2]))
print(dialog[dialog['fork1'][2][1]][2])
while True:
    phrase = dialog[phrase_code]
    if phrase[0] == 'code':
        print(phrase[1])
    else:
        print('--{}--\n{}'.format(phrase[0], phrase[1]))

    if type(phrase[2]) is str:
        phrase_code = phrase[2]
    else:
        fork = phrase[2]
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



##phrase_code = 'begin'
##fork = 0
##while True:
##    if fork:
##        phrase = dialog[phrase_code][branch_num]
##        branch_num += 1
##        print('--{}--\n{}'.format(phrase[0], phrase[1]))
##        if len(phrase[2]) == branch_num:
##            fork = 0
##    else:
##        phrase = dialog[phrase_code]
##        if phrase[0] == 'code':
##            print(phrase[1])
##        else:
##            print('--{}--\n{}'.format(phrase[0], phrase[1]))
##        choice = input()
##        if type(phrase[2]) == 'str':
##            phrase_code = phrase[2]
##        else:
##            #phrase_code = phrase[2][0]
##            fork = phrase[2]
##            branch_num = 0
