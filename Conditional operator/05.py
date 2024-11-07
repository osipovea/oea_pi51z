a = input("Введи строку 1: ")
b = input("Введи строку 2: ")
c = input("Введи строку 3: ")
if ((a.lower() == "раз" or a.lower() =="один") and b.lower() == "два" and c.lower() == "три") or (a == "1" and b == "2" and c == "3"):
   print("ГОРИ")
else:
    print("НЕ ГОРИ")
