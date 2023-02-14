# Напишите программу, которая на вход принимает два 
# числа A и B,и возводит число А в целую степень B с 
# помощью рекурсии. >



num = int(input('Введите число А: '))
deg = int(input('Введите его степень В: '))

def power(num,deg):
    if (deg == 1):
        return(num)
    if (deg !=1):
        return(num * power(num,deg - 1))
print('Возведение числа А в степень В равно:',power(num,deg))
    