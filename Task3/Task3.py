try:
    n = int(input("Введите количество элементов массива: "))
    if n > 1:
        array = [i for i in range(n)]
        print("Ваш массив: ", *array)

        array = [i for i in range(n)
        if i % 3 == 0]
        print("Массив чисел кратных трем: ", *array)
    else:
        print("Количество элементов массива должно быть больше 1")
except ValueError:
    print('Вы ввели не число!')
