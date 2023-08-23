from random import randrange
#some_changes

def is_valid(arg):
    return arg.isdigit() and int(arg) in range(1, 100)


def in_range():
    while True:
        num = input('Введи число от 1 до 100:')
        if is_valid(num):
            return int(num)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def comparing():
    count = 0
    while True:
        n = in_range()
        count += 1
        if n < rand_n:
            print('Ваше число меньше загаданного, попробуйте еще разок\n')
        elif n > rand_n:
            print('Ваше число больше загаданного, попробуйте еще разок\n')
        else:
            print(f'\nВы угадали число за {count} попыток, поздравляем!')
            break


def game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        global rand_n
        rand_n = randrange(1, 100)
        comparing()
        if continue_game():
            continue
        else:
            break


def continue_game():  # Предложение продолжить игру
    ans = input('Сыграем еще разок? ("да"/"нет")\n').lower()
    while True:
        if ans not in ('y', 'да', 'n', 'нет'):
            ans = input('Да или нет("д"/"н")?\n').lower()
        elif ans in ('n', 'нет'):
            print('Спасибо, что играли в числовую угадайку ☺. Еще увидимся...')
            return False
        else:
            return True


game()
