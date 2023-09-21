import math
def add():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    result = first_number + second_number
    print('Ответ:', result)
    return result
def sub():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    result = first_number - second_number
    print('Ответ:', result)
    return result
def div():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    if second_number == 0:
        result = None
        print('Деление на ноль невозможно')
    else:
        result = float(first_number / second_number)
        print('Ответ:', result)
    return result
def mult():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    result = first_number * second_number
    print('Отве:', result)
    return result
def step():
    first_number = int(input('Введите число: '))
    second_number = int(input('Введите степень: '))
    result = first_number ** second_number
    print('Отве:', result)
    return result
def sqrt():
    number = int(input('Введите число: '))
    if number >= 0:
        result = number ** (0.5)
        print('Ответ:', result)
    else:
        result = None
        print('Корень из отрицательного числа не существует')
    return result
def sine():
    number = int(input('Введите число: '))
    result = math.sin(number)
    print('Ответ:', result)
    return result
def cosine():
    number = int(input('Введите число: '))
    result = math.cos(number)
    print('Ответ:', result)
    return result
def tangent():
    number = int(input('Введите число:'))
    result = math.tan(number)
    print('Ответ:', result)
    return result
def factorial():
    number = int(input('Введите число:'))
    result = math.factorial(number)
    print('Ответ:', result)
    return result
while True:
    operation = int(input('Выберите математическую операцию: \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в степень -- 5\nВычисление квадратного корня -- 6\nВычисление синуса -- 7\nВычисление косинуса -- 8\nВычисление тангенса -- 9\nВычисление факториала -- 10\nНапишите 11 для завершения работы калькулятора\n'))
    if operation == 1:
        add()
    if operation == 2:
        sub()
    if operation == 3:
        mult()
    if operation == 4:
        div()
    if operation == 5:
        step()
    if operation == 6:
        sqrt()
    if operation == 7:
        sine()
    if operation == 8:
        cosine()
    if operation == 9:
        tangent()
    if operation == 10:
        factorial()
    if operation == 11:
        print('Калькулятор завершил свою работу!')
        break