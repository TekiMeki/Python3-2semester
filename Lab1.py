def encode(s: str, k: int):
    mass=list(map(int, input("Введите последовательность {k}: ".format(k=k)).split()))
    with open('crypto.txt', 'r') as reader:
        print(reader.readline())
    out=''
    if len(mass)>k:
        print('Ошибка: введено больше чисел чем требует посследовательность')
    for x in mass:
        if x >=k:
            print('Ошибка: введённая последовательность имеет число превышающее значение ключа')
    while len(s) % k!=0:
        s+='ь'
    for i in range(0, len(s), k):
        stroka=s[i: i+k]
        for j in mass:
            out+=stroka[j]
    return out
with open('crypto.txt', 'w') as writer:
    codetostr=input('Введите шифруемую строку: ')
    writer.write(codetostr)
    writer.write('\n')
    keycode =input('Введите ключ для шифрования: ')
    writer.write(keycode)
    writer.write('\n')

with open('crypto.txt', 'r') as reader:
    encodestr=reader.readline()
    keyencode=reader.readline()

    # Як умру, то поховайте мене на могилі, cеред степу широкого
print('Исходная строка:', encodestr, 'Ключ:', keyencode)
print('\nКодируем:', encode(encodestr, int(keyencode)))
