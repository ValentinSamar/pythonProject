def  int_func(slovo):
    uslovie='qwertyuiopasdfghjklzxcvbnm'
    return slovo.title() if not set(slovo).difference(uslovie) else False
slovo=input('Vvedite slova razdelenie probelami').split()
for s in slovo:
    resh=int_func(s)
    if resh:
        print(int_func(s),' ')