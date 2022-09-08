price = 0
while True:
    try:
        tickets = int(input("Введите количество билетов для онлайн-конференции: "))
        if type(tickets) == int:
            break
    except ValueError:
        print("Введите корректное количество!")
for i in range(tickets):
    i += 1
    while True:
        try:
            age = int(input(f"Возраст посетителя № {i} : "))
            if age >= 25:
                price += 1390
                print("Цена билета: 1390 руб.")
            elif 25 > age >= 18:
                price += 990
                print("Цена билета: 990 руб.")
            else:
                print("Проход бесплатный")
            if type(age) == int:
               break
        except ValueError:
            print("Введите корректный возраст!")

if tickets < 3:
    print(f"Сумма к оплате: {price} руб.")
else:
    discount_price = int(price * 0.9)
    print(f"Сумма к оплате: {discount_price} руб. За регистрацию группы больше трех человек скидка 10%.")