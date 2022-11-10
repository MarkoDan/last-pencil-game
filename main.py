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

while True:
    if pencils < 1:
        print(f'{name} won!')
        break
    print('|' * pencils)
    print(f'{name}\'s turn')
    while True:
        if name == 'Jack':
            if pencils % 4 == 0:
                print('3')
                pencils -= 3
            elif pencils % 4 == 3:
                print('2')
                pencils -= 2
            elif pencils % 4 == 2:
                print('1')
                pencils -= 1
            elif pencils == 1:
                print(pencils)
                pencils -= 1
            else:
                random_choise = random.randint(1,3)
                print(random_choise)
                pencils -= random_choise
            break
        else:
            choice = input()
            if choice not in ('1', '2', '3'):
                print("Possible values: '1', '2' or '3'")
            elif int(choice) > pencils:
                print('Too many pencils were taken')
            else:
                pencils -= int(choice)
                break
    
    name = 'John' if name == 'Jack' else 'Jack'