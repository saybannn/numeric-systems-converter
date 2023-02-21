print('Здравствуйте, дорогой юзер! :) Данная программа преобразует положительные числа из одной системы '
      'счисления в другую.\nЧтобы выбрать необходимое вам преобразование, введите соответствующее '
      'число из заданых ниже: ')
print()


def is_decimal(input_str):
    try:
        int(input_str, 10)
        return True
    except ValueError:
        return False


def is_binary(input_str):
    try:
        int(input_str, 2)
        return True
    except ValueError:
        return False


def is_octal(input_str):
    try:
        int(input_str, 8)
        return True
    except ValueError:
        return False


def is_hexadecimal(input_str):
    try:
        int(input_str, 16)
        return True
    except ValueError:
        return False


while True:
    print('10-> 2 нажать 1\n--------------')
    print('10-> 8 нажать 2\n--------------')
    print('10-> 16 нажать 3\n--------------')
    print('2-> 10 нажать 4 \n--------------')
    print('2-> 8 нажать 5\n--------------')
    print('2-> 16 нажать 6\n--------------')
    print('8-> 10 нажать 7\n--------------')
    print('8-> 2 нажать 8\n--------------')
    print('8-> 16 нажать 9\n--------------')
    print('16-> 10 нажать 10\n--------------')
    print('16-> 2 нажать 11\n--------------')
    print('16-> 8 нажать 12\n--------------')

    ask = input('Выберите операцию по номеру: ').strip()

    if ask == '1':
        num = input('10: ').strip()
        if is_decimal(num) and len(num) != 0 and num[0] != '-':
            num_to = bin(int(num))
            print(f'{num}(10) = {num_to[2:]}(2)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное десятичное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '2':
        num = input('10: ').strip()
        if is_decimal(num) and len(num) != 0 and num[0] != '-':
            num_to = oct(int(num))
            print(f'{num}(10) = {num_to[2:]}(8)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное десятичное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '3':
        num = input('10: ').strip()
        if is_decimal(num) and len(num) != 0 and num[0] != '-':
            num_to = hex(int(num))
            print(f'{num}(10) = {num_to[2:].upper()}(16)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное десятичное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '4':
        num = input('2: ').strip()
        if is_binary(num) and len(num) != 0 and num[0] != '-':
            binary = '0b' + str(num)
            num_to = eval(binary)
            print(f'{num}(2) = {num_to}(10)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное двоичное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '5':
        num = input('2: ').strip()
        if is_binary(num) and len(num) != 0 and num[0] != '-':
            binary = '0b' + str(num)
            num_to = oct(eval(binary))
            print(f'{num}(2) = {num_to[2:]}(8)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное двоичное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '6':
        num = input('2: ').strip()
        if is_binary(num) and len(num) != 0 and num[0] != '-':
            binary = '0b' + str(num)
            num_to = hex(eval(binary))
            print(f'{num}(2) = {num_to[2:].upper()}(16)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное двоичное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '7':
        num = input('8: ').strip()
        if is_octal(num) and len(num) != 0 and num[0] != '-':
            octal = '0o' + str(num)
            num_to = eval(octal)
            print(f'{num}(8) = {num_to}(10)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное восьмеричное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '8':
        num = input('8: ').strip()
        if is_octal(num) and len(num) != 0 and num[0] != '-':
            octal = '0o' + str(num)
            num_to = bin(eval(octal))
            print(f'{num}(8) = {num_to[2:]}(2)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное восьмеричное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '9':
        num = input('8: ').strip()
        if is_octal(num) and len(num) != 0 and num[0] != '-':
            octal = '0o' + str(num)
            num_to = hex(eval(octal))
            print(f'{num}(8) = {num_to[2:].upper()}(16)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное восьмеричное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '10':
        num = input('16: ').strip()
        if is_hexadecimal(num) and len(num) != 0 and num[0] != '-':
            hexadecimal = '0x' + str(num.lower())
            num_to = eval(hexadecimal)
            print(f'{num.upper()}(16) = {num_to}(10)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное шестнадцатиричное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '11':
        num = input('16: ').strip()
        if is_hexadecimal(num) and len(num) != 0 and num[0] != '-':
            hexadecimal = '0x' + str(num)
            num_to = bin(eval(hexadecimal))
            print(f'{num.upper()}(16) = {num_to[2:]}(2)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное шестнадцатиричное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    elif ask == '12':
        num = input('16: ').strip()
        if is_hexadecimal(num) and len(num) != 0 and num[0] != '-':
            hexadecimal = '0x' + str(num)
            num_to = oct(eval(hexadecimal))
            print(f'{num.upper()}(16) = {num_to[2:]}(8)')
            ask_to = input('Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Необходимо ввести положительное шестнадцатиричное число! '
                           'Нажмите любую клавишу для продолжения... ').strip()
            continue

    else:
        print('Пожалуйста, введите число из списка заданых. '
              'Нажмите любую клавишу для продолжения. Для выхода нажмите \'q\': ', end='')
        ask_to = input().strip()
        if ask_to.lower() == 'q':
            break
        else:
            continue

print('Удачи!')
input('...')
