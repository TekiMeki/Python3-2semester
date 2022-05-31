from random import randint, choice
from re import findall

from memory import Key, Limit, keysCrypt, listSyllables


def main():
    ############################################################################
    # ------------------------ Специальные символы ----------------------------#
    # Количество занимаемого места памяти: 4
    # listSpecial = ('<-', '->', '<+', '+>')
    #
    # position = len(listWord) + len(listSyllables) + 278  # 423 + 108 + 278 = 809
    # keysSpecial = {listSpecial[x]: Key[x + position] for x in range(len(listSpecial))}
    # -------------------------------------------------------------------------#


    # Опция шифрования/расшифрования
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit

    # Открытое сообщение
    startMessage = input("Write the message: ")


    # Вывод финального сообщения
    finalMessage = encryptDecrypt(cryptMode, startMessage)
    print("Final message:", finalMessage)

def regular(text):              # Функция с регулярным выражением разделения трёх чисел
    return findall(r"[0-9]{3}", text)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def encryptDecrypt(mode, message, final="", string=""):
    global listWord

    # ---------------------- Омофоническое шифрование -------------------------#
    position =278
    keysCode = {listWord[x]: Key[x + position] for x in range(len(listWord))}

    # ----------------------- Замена слогов и символов ------------------------#
    position = len(listWord) + 278  # 423 + 278 = 701
    keysSyllables = {listSyllables[x]: Key[x + position] for x in range(len(listSyllables))}

    # --------------------------- Ложные символы ------------------------------#
    position = len(listWord) + len(listSyllables) + 278
    traps = tuple([Key[x] for x in range(position, Limit)])

    # Удаление неиспользуемых элементов
    del listWord, position

    ## Шифрование
    if mode == 'E':

        listNum = findall(r"[0-9]{3}", message)
        for i in listNum:
            message = message.replace(i, '00' + i)

        # Разделение списка на слова
        secondText = findall(r"[^\s]+", message)

        # Удаление неиспользуемых элементов
        del message

        # Внедрение в код специальных символов
        # for indexWord in range(len(secondText)):
        #     if secondText[indexWord] in keysSpecial:
        #         secondText[indexWord] = keysSpecial[secondText[indexWord]]

        # Кодирование слов на числа
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysCode:
                secondText[indexWord] = keysCode[secondText[indexWord]]

        # Замена слогов на числа
        for indexWord in range(len(secondText)):
            for syllable in keysSyllables:
                if syllable in secondText[indexWord]:
                    secondText[indexWord] = secondText[indexWord].replace(syllable, keysSyllables[syllable])

        # Разделение всех слов на символы
        for indexWord in range(len(secondText)):
            secondText[indexWord] = list(secondText[indexWord])
        for indexWord in range(len(secondText)):
            secondText[indexWord].append(' ')

        # Шифрование всех символов на числа
        for indexWord in range(len(secondText)):
            for indexSymbol in range(len(secondText[indexWord])):
                symbol = secondText[indexWord][indexSymbol]
                if symbol in keysCrypt:
                    length = len(keysCrypt[symbol])
                    secondText[indexWord][indexSymbol] = keysCrypt[symbol][randint(0, length - 1)]

        # Соединение всех чисел в одну строку и разделение по три
        for word in secondText:
            string += "".join(word)
        finalList = list(regular(string))

        # Внедрение в код ложных символов
        for indexList in range(len(finalList)):
            randSwitch = randint(0, 2)
            randPosition = randint(0, len(finalList))
            if not randSwitch:
                finalList.insert(randPosition, choice(traps))

        # Занесение в переменную final зашифрованный текст
        for word in finalList:
            final += "".join(word)
        return ".".join(regular(final))

    ## Расшифрование
    else:
        # Перебор всех 'XYZ' чисел в зашифрованном сообщении
        for symbolText in regular(message):
            # for element in keysSpecial:  # Перебор всех специальных символов
            #     if symbolText == keysSpecial[element]:
            #         final += element
            for word in keysCode:  # Перебор всех кодов
                if symbolText == keysCode[word]:
                    final += word
            for syllable in keysSyllables:  # Перебор всех слогов
                if symbolText == keysSyllables[syllable]:
                    final += syllable
            for symbol in keysCrypt:  # Перебор всех шифров
                if symbolText in keysCrypt[symbol]:
                    final += symbol
        listWord = findall(r"[^\s]+", final)
        listNum = findall(r"[0-9]{3}", final)

        # Опции специальных символов
        # for _ in range(len(listWord)):
        #     for element in keysSpecial:
        #         if element in listWord:
        #             if element == '<-':
        #                 del listWord[listWord.index(element) - 1]
        #                 listWord.remove(element)
        #             elif element == '->':
        #                 del listWord[listWord.index(element) + 1]
        #                 listWord.remove(element)
        #             elif element == '<+':
        #                 listWord[listWord.index(element)] = listWord[listWord.index(element) - 1]
        #             elif element == '+>':
        #                 listWord[listWord.index(element)] = listWord[listWord.index(element) + 1]
        #             else:
        #                 pass
        final = " ".join(listWord)
        listNum1 = findall(r"[0]{2}[0-9]{3}", final)
        for i in listNum1:
            final = final.replace(i, i[2:])
        for i in listNum:
            try:
                final = final.replace(i, get_key(keysCode, i))
            except TypeError:
                pass
        for i in listNum:
            try:
                final = final.replace(i, get_key(keysSyllables, i))
            except TypeError:
                pass
        return final


if __name__=="__main__":
    main()