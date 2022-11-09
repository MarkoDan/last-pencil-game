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
bot = ''
if name == 'John':
    bot = 'John'
elif name == 'Jack':
    bot = 'Jack'



while True:
    if pencils < 1:
        print(f'{name} won!')
        break
    print('|' * pencils)
    print(f'{name}\'s turn')
    while True:
        choice = input()
        if choice not in ('1', '2', '3'):
            print("Possible values: '1', '2' or '3'")
        elif int(choice) > pencils:
            print('Too many pencils were taken')
        else:
            break

    while True:
        random_choice = random.randint(1, 3)
        print(f"{bot}'s turn")
        print(random_choice)
        if random_choice not in (1, 2, 3):
            print("Possible values: '1', '2' or '3'")
        else:
            break
    pencils -= int(choice)
    pencils -= int(random_choice)
    if name == 'Jack':
        bot = 'John'
    else:
        bot = 'Jack'
