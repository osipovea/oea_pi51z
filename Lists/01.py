n = int(input("Введите кол-во покупок :"))
products = []
for i in range(n):
  product = input("Введите название товара: ")
  products.append(product)
for product in products:
  print(product)
