a = int(input("Введите число 1 :"))
b = int(input("Введите число 2 :"))
c = input("Введите знак математической операции или любой другой символ :")

if c == "+":print(a+b)
elif c == "-":print(a-b)
elif c == "*":print(a*b)
elif c == "/" and b != 0:print (a/b)
else: print("888888")
