houses = input("Введите номера домов из первого списка, разделенные пробелами: ").split()
houses1 = input("Введите номера домов из второго списка, разделенные пробелами: ").split()
houses_set = set(houses)
houses_set1 = set(houses1)
intersection = houses_set.intersection(houses_set1)
if intersection:
 print("Номера, встретившиеся в обоих списках:", intersection )
else:
 print("EMPTY")
