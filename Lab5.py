from os import system

global IV
IV = '1010111'


def main():
    menu = '''
   ------------Menu-------------
   1 - Зашифровать сообщение
   -----------------------------
                       q - Выход
   '''
    flag = True
    while True:
        answer = input(menu)
        if answer == 'q' or answer == 'Q':
            exit()

        elif answer == '1':
            bin_text = ''
            while len(bin_text) < len(IV):
                bin_text = input("Enter text (length > %d): " % (len(IV) + 1))
            bin_key = ''
            while len(bin_key) != len(IV):
                bin_key = input("Enter key (length = %d): " % (len(IV)))
            Z = '' + IV
            schetchik = 0
            while len(Z) != len(bin_text):
                a = 0
                for count, c in enumerate(bin_key):
                    a ^= int(c) * int(Z[schetchik + count])
                Z += str(a)
                schetchik += 1
            Y = ''
            for count, z in enumerate(Z):
                Y += str(int(z) ^ int(bin_text[count]))
            print('Encrypt text: ', Y)

            if flag:
                menu = '''
   ------------Menu-------------
   1 - Расшифровать сообщение
   -----------------------------
                       q - Выход
   '''
                flag = False
            else:
                menu = '''
   ------------Menu-------------
   1 - Зашифровать сообщение
   -----------------------------
                       q - Выход
   '''
                flag = True

        else:
            system('clear')
        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == '__main__':
    main()