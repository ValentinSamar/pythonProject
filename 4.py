def my_func(x,y):
    return 1 if y==0 else my_func(x,y+1)*1/x
print(my_func(10,-4))