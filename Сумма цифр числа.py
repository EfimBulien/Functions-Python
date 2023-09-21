
def sum_digits(number):
    suma = 0
    while number > 0:
        digit = number % 10
        suma = suma + digit
        number = number // 10
    print(suma)
while True:
    number = int(input("Введите число: "))
    sum_digits(number)