def my_func(n1=int(input('Введите чило')),n2=int(input('Введите чило')),n3=int(input('Введите чило'))):
    my_list=[n1,n2,n3]
    try:
        my_list.remove(min(my_list))
        return  sum(my_list)
    except TypeError:
        return "ВВЕДИТЕ ЧИСЛА!!!"
print(my_func())