import random

print('How many pencils would you like to use:')
while True:
    pencils = input()
    if not pencils.isdigit():
        print('The number of pencils should be numeric')
    elif int(pencils) < 1:
        print('The number of pencils should be positive')
    else:
        pencils = int(pencils)
        break

name = input('Who will be the first (John, Jack):')
while name not in ('John', 'Jack'):
    print('Choose between John and Jack')
    name = input()
bot = name

second_player = ''
if bot == 'John':
    second_player = 'Jack'
else:
    second_player = 'John'

while True:
    random_choice = random.randint(1, 3)
    print('|' * pencils)
    print(f"{bot}'s turn")
    print(random_choice)
    if random_choice not in (1, 2, 3):
        print("Possible values: '1', '2' or '3'")
    else:
        pencils -= random_choice
        print('|' * pencils)
        print(f"{second_player}'s turn")
        choice = input()
        if choice not in ('1', '2', '3'):
            print("Possible values: '1', '2' or '3'")
        elif int(choice) > pencils:
            print('Too many pencils were taken')
        else:

            pencils -= int(choice)
            choice = int(choice)
        if pencils - random_choice == 0:
            print(f"{bot} won!")
            bot_won = True
            break
        elif pencils - choice == 0:
            print(f"{second_player} won!")
            break

    if pencils == 0:
        break
