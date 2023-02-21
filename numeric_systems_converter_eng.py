print('Hi, dear user! :) This program converts positive numbers from one numeric system '
      'to another.\nTo select the conversion you need, enter the appropriate '
      'number from the given below: ')
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
    print('10-> 2 press 1\n--------------')
    print('10-> 8 press 2\n--------------')
    print('10-> 16 press 3\n--------------')
    print('2-> 10 press 4 \n--------------')
    print('2-> 8 press 5\n--------------')
    print('2-> 16 press 6\n--------------')
    print('8-> 10 press 7\n--------------')
    print('8-> 2 press 8\n--------------')
    print('8-> 16 press 9\n--------------')
    print('16-> 10 press 10\n--------------')
    print('16-> 2 press 11\n--------------')
    print('16-> 8 press 12\n--------------')

    ask = input('Choose the operation by number: ').strip()

    if ask == '1':
        num = input('10: ').strip()
        if is_decimal(num) and len(num) != 0 and num[0] != '-':
            num_to = bin(int(num))
            print(f'{num}(10) = {num_to[2:]}(2)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive decimal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '2':
        num = input('10: ').strip()
        if is_decimal(num) and len(num) != 0 and num[0] != '-':
            num_to = oct(int(num))
            print(f'{num}(10) = {num_to[2:]}(8)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive decimal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '3':
        num = input('10: ').strip()
        if is_decimal(num) and len(num) != 0 and num[0] != '-':
            num_to = hex(int(num))
            print(f'{num}(10) = {num_to[2:].upper()}(16)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive decimal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '4':
        num = input('2: ').strip()
        if is_binary(num) and len(num) != 0 and num[0] != '-':
            binary = '0b' + str(num)
            num_to = eval(binary)
            print(f'{num}(2) = {num_to}(10)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive binary number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '5':
        num = input('2: ').strip()
        if is_binary(num) and len(num) != 0 and num[0] != '-':
            binary = '0b' + str(num)
            num_to = oct(eval(binary))
            print(f'{num}(2) = {num_to[2:]}(8)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive binary number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '6':
        num = input('2: ').strip()
        if is_binary(num) and len(num) != 0 and num[0] != '-':
            binary = '0b' + str(num)
            num_to = hex(eval(binary))
            print(f'{num}(2) = {num_to[2:].upper()}(16)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive binary number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '7':
        num = input('8: ').strip()
        if is_octal(num) and len(num) != 0 and num[0] != '-':
            octal = '0o' + str(num)
            num_to = eval(octal)
            print(f'{num}(8) = {num_to}(10)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive octal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '8':
        num = input('8: ').strip()
        if is_octal(num) and len(num) != 0 and num[0] != '-':
            octal = '0o' + str(num)
            num_to = bin(eval(octal))
            print(f'{num}(8) = {num_to[2:]}(2)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive octal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '9':
        num = input('8: ').strip()
        if is_octal(num) and len(num) != 0 and num[0] != '-':
            octal = '0o' + str(num)
            num_to = hex(eval(octal))
            print(f'{num}(8) = {num_to[2:].upper()}(16)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive octal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '10':
        num = input('16: ').strip()
        if is_hexadecimal(num) and len(num) != 0 and num[0] != '-':
            hexadecimal = '0x' + str(num.lower())
            num_to = eval(hexadecimal)
            print(f'{num.upper()}(16) = {num_to}(10)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive hexadecimal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '11':
        num = input('16: ').strip()
        if is_hexadecimal(num) and len(num) != 0 and num[0] != '-':
            hexadecimal = '0x' + str(num)
            num_to = bin(eval(hexadecimal))
            print(f'{num.upper()}(16) = {num_to[2:]}(2)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive hexadecimal number! '
                           'Click any button to continue... ').strip()
            continue

    elif ask == '12':
        num = input('16: ').strip()
        if is_hexadecimal(num) and len(num) != 0 and num[0] != '-':
            hexadecimal = '0x' + str(num)
            num_to = oct(eval(hexadecimal))
            print(f'{num.upper()}(16) = {num_to[2:]}(8)')
            ask_to = input('Click any button to continue. Press \'q\' to exit: ').strip()
            if ask_to.lower() == 'q':
                break
            else:
                continue
        else:
            ask_to = input('Need to enter a positive hexadecimal number! '
                           'Click any button to continue... ').strip()
            continue

    else:
        print('Please, enter a number from the given list. '
              'Click any button to continue. Press \'q\' to exit: ', end='')
        ask_to = input().strip()
        if ask_to.lower() == 'q':
            break
        else:
            continue

print('Good luck!')
input('...')
