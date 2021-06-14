def p_inf(**kwargs):
    return ' '.join(kwargs.values())
name=input('Введите имя-')
surname=input('Введите фамилию-')
god_r=input('Введите год рождения-')
gorod=input('Введите город-')
email=input('Введите почту-')
tel=input('Введите телефон-')
print(p_inf(имя=name, фамилия=surname, год_рождения=god_r, город=gorod, почта=email, телефон=tel))
