import sys
print(f"{' ПРОГРАММА Система управления кофейней ':=^90}")

flag1=False
zakazas=0
stat_zakaz=[]
histori_zakaz=[]
tuple_menu = (('Кофе', 160 ),('Чай', 90),('Сок',100),('Лимонад', 110),('Булочка с повидлом',210),
              ('Булочка с мясом',240),('Булочка с капустой',200),('Пицца с калбасой',350),('Пицца маргарита',400))
tuple_zakaz = ()
while True:
    print("""1. Посмотреть меню кофейни
2. Создать новый заказ
3. Расчитать сумму заказа
4. Статистика дня
5. Зкрыть смену """)
    while True:
        try:
            punkt_menu = int(input("Выберите действие: "))
            break
        except ValueError:
            print("Ошибка! Пункт меню нужно писать цифрами!")
    match punkt_menu:
        case 1:
            print("-"*49)
            print(f"|{'№':^5}|{'Блюдо':^25}|{'Цена':^15}|")
            print("-"*49)
            for i, elem in enumerate(tuple_menu):
                print(f"|{i+1:^5}|{elem[0]:<25}|{elem[1]:^15}|")
                print("-"*49)
                flag=True
        case 2:
            tuple_zakaz = ()
            summ_zakaza=0 
            print("-"*49)
            print(f"|{'№':^5}|{'Блюдо':^25}|{'Цена':^15}|")
            print("-"*49)
            for i, elem in enumerate(tuple_menu):
                print(f"|{i+1:^5}|{elem[0]:<25}|{elem[1]:^15}|")
                print("-"*49)
            while True:
                zakaz = input(f"Введите позиции через пробел от 1 до {len(tuple_menu)}: ")
                try:
                    list_zakaz = list(map(int, zakaz.split()))
                    break
                except ValueError:
                    print("Ошибка! Вводите только числа через пробел (например: 1 3 5)")
            for i in list_zakaz:
                i = i-1
                if 0<= i < len(tuple_menu):
                    blyudo = tuple_menu[i]
                    tuple_zakaz += (blyudo,)
                else: 
                    print(f"Позиции {i+1} нет в меню!")                                
            for blyudo in tuple_zakaz:
                summ_zakaza +=blyudo[1]
            if len(tuple_zakaz)==0:
                print("Ваш заказ пуст!")
            else:
                print(f"Ваш заказ {tuple_zakaz}")
            flag1=True
            
        case 3:
            if flag1 == True and len(tuple_zakaz)!=0:
                print("\n" + "="*50)
                print(f"ЧЕК №{zakazas+1}")
                print("="*50)
                print(f"{'№':<5} {'Наименование':<30} {'Цена':>10}")
                print("-"*50)

                for nomer, blyudo in enumerate(tuple_zakaz, start=1):
                    print(f"{nomer:<5} {blyudo[0]:<30} {blyudo[1]:>10} руб.")

                print("-"*50)
                print(f"{'ИТОГО К ОПЛАТЕ:':<35} {summ_zakaza:>10} руб.")
                print("="*50)
                print("Спасибо за покупку! ")
                print("="*50)
                zakazas+=1
                histori_zakaz.append(summ_zakaza)

                flag1 = False
                tuple_zakaz = ()
                summ_zakaza = 0
            else:
                print("Извените но на данный момент заказа нет.")
        case 4:
            if len(histori_zakaz)==0:
                print("Статистики пока нет.")
            else:

                print("-"*53)  
                print(f"|{'Количество заказов':<30}|{zakazas:^20}|") 
                print(f"|{'Максимальная сумма заказа':<30}|{max(histori_zakaz):^20.2f}|") 
                print(f"|{'Средний чек':<30}|{sum(histori_zakaz)/len(histori_zakaz):^20.2f}|") 
                print(f"|{'Общаяя сумма заказов':<30}|{sum(histori_zakaz):^20.2f}|") 
                print("-"*53)  

        case 5:
            print("Выход...")
            sys.exit()
        case _:
            print("Неверный пункт меню!")

