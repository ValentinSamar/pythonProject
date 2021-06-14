def sn():
    s=0
    while True:
        in_list=input('Веедите число или q для выхода из программы').split()
        for n in in_list:
            if n=='q':
                return s
            else:
                try:
                    s+=int(n)
                except ValueError:
                    print('Для выхода нажмите q')
        print(f'Сумма чисел={s}')
print(sn())