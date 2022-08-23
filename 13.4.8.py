try:
    a = int(input("Введите целое число:"))
    if a == None:
        raise ValueError
except ValueError as error:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели {a}")

print("Выход из программы")
