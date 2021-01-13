def sal():
    try:
        time = float(input('Введите количество часов:\n'))
        salary = int(input('Введите почасовую ставку сотрудника:\n'))
        bonus = int(input('Введите размер премиальных:\n'))
        result = (time * salary) + bonus
        print(f'Расчёт заработной платы сотрудника выполнен.\nЗП: {result} рублей')
    except ValueError:
        return print('Ошибка: введённое - не число.')
sal()
