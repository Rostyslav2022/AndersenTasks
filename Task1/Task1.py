try:
    number = float(input("Введите число: "))
    if number > 7:
        print("Привет")
    else:
        print("Hasta la vista, baby")
except ValueError:
    print('Вы ввели не число!')
