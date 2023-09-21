def is_even(number):
    if number % 2 ==0:
        print("True")
    else:
        print ("False")
while True:
    number = int(input("Введите число: "))
    is_even(number)