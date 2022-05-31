import math

factorial = 1
print('Факториал 10!')
for x in range (2, 11):
    factorial *= x
    print(factorial)

try:
    print('Введите переменную а')
    a = int(input())
    print('Введите переменную b')
    b = int(input())
    print('Введите переменную с')
    c = int(input())
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print('D = ' + str(D))
        print('х1 = ' + str(x1) + '\nх2 = ' + str(x2))
    elif D == 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print('D = ' + str(D))
        print('х1 = х2 = ' + str(x1))
    else:
        print('D = ' + str(D))
        print('Корней уравнения не существует')
except ValueError:
    print('К сожалению, входные данные не корректно')