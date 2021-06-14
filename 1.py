def div(ch_1, ch_2):
    try:
        ch_1, ch_2= int(ch_1), int(ch_2)
        div_num= ch_1 / ch_2
    except ValueError:
        return "ValueError"
    except ZeroDivisionError:
        return "ZeroDivisionError НЕТ"
    return round(div_num,4)
print(div(input('Ввведите первое число'),input('Ввведите второе число')))