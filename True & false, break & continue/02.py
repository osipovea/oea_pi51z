if True:
    print('Эта строка будет выведена на экран.')
else:
    print('Эта строка никогда не будет выведена на экран.')

a = input()
b = input()
# Теперь переменная equal равна True, если строки a и b равны,и False
# в противном случае
equal = (a == b)
if equal and len(a) < 6:
    print('Вы ввели два коротких одинаковых слова.')