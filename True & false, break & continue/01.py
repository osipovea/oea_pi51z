if True:
    print('Эта строка будет выведена на экран.')
else:
    print('Эта строка никогда не будет выведена на экран.')
a = int(input("Введите число 1: "))
b = int(input("Введите число 2, где число 2 больше числа 1: "))
if a < b:
    for i in range(a,b+1):
        if i % 3 ==0 and i % 5 ==0:
            print('FizzBuzz')
        elif i % 3==0:
            print('Fizz')
        elif i % 5==0:
            print('Buzz')
        else:
            print(i)
else:
    print('Число 2 меньше числа 1')