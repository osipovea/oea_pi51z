password = input("Введите пароль: ")
password1 = input("Повторите пароль: ")
while len(password) < 8:
    print("Короткий!")
    password = input("Введите пароль: ")
    password1 = input("Повторите пароль: ")
while password != password1:
    print("Различаются.")
    password = input("Введите пароль: ")
    password1 = input("Повторите пароль: ")
print("OK.")

