n = int(input("Дней наблюдения"))
days = 0
for i in range(n):
    temp = float(input("Введите температуру"))
    if temp < 22:
        days+= 1
print("Наблюдения завершены! Количество полных недель составляет: ", days // 7)