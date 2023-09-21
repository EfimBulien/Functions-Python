def rectangle_area(width, height):
    if width <= 0 or height <=0:   
        print("Неверные значения")
    else:
        print("Площадь прямоугольника = ", (width * height))
while True:
    print("Введите ширину прямоугольника")
    width = int(input())
    print("Введите высоту прямоугольника")
    height = int(input())
    rectangle_area(width, height)