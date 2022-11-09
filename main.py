import string
numbers = [1, 2, 3]
print('How many pencils would you like to use:')
while True:
    number_of_pencils = input()
    if str(number_of_pencils) in string.ascii_letters or number_of_pencils in string.punctuation or not number_of_pencils.isdigit():
        print('The number of pencils should be numeric')
        continue
    elif int(number_of_pencils) <= 0:
        print('The number of pencils should be positive')
        continue
    else:
        number_of_pencils = int(number_of_pencils)
    player1 = 'John'
    player2 = 'Jack'
    print(f'Who will be the first ({player1}, {player2})')

    while True:
        player_choise = input()
        if player_choise == player1 or player_choise == player2:
            print(number_of_pencils * '|')
            while number_of_pencils > 0:

                print(f"{player_choise}'s turn")
                number = input()
                if number not in string.digits:
                    print(f"Possible values: {numbers}")
                    continue
                elif int(number) not in numbers:
                    print(f"Possible values: {numbers}")
                    continue
                else:
                    number = int(number)
                    number_of_pencils = number_of_pencils - number
                    print(number_of_pencils * '|')
                    if number_of_pencils == 0:
                        print(f'{player_choise} won!')
                        break
                    elif number_of_pencils < 0:
                        if player_choise == player1:
                            print('To many pencils were taken')
                            print(f'{player2} won!')
                            break

                        else:
                            print('To many pencils were taken')
                            print(f'{player1} won!')
                            break
                    else:

                        if player_choise == player1 and number_of_pencils != 0:
                            while True:
                                print(f"{player2}'s turn")
                                number = input()
                                if number not in string.digits:
                                    print(f"Possible values: {numbers}") 
                                    continue
                                elif int(number) not in numbers:
                                    print(f"Possible values: {numbers}") 
                                    continue
                                else:
                                    number = int(number)
                                    if number > number_of_pencils:
                                        print('To many pencils were taken')
                                        print(f'{player1} won!')
                                        break
                                    else:
                                        number_of_pencils = number_of_pencils - number
                                        print(number_of_pencils * '|')
                                        if number_of_pencils <= 0:
                                            print(f'{player2} won!')


                                break

                        elif player_choise == player2 and number_of_pencils != 0:
                            while True:
                                print(f"{player1}'s turn")
                                number = input()
                                if number not in string.digits:
                                    print(f"Possible values: {numbers}") 
                                    continue
                                elif int(number) not in numbers:
                                    print(f"Possible values: {numbers}") 
                                    continue
                                else:
                                    number = int(number)
                                    if number > number_of_pencils:
                                        print('To many pencils were taken')
                                        print(f'{player2} won!')
                                        break
                                    else:
                                        number_of_pencils = number_of_pencils - number
                                        print(number_of_pencils * '|')
                                    if number_of_pencils <= 0:
                                        print(f'{player1} won!')


                                break

                    if number_of_pencils <= 0:
                        break

            break

        else:
            print(f"Choose between '{player1}' or '{player2}'")
    
    break
    
    
        


    