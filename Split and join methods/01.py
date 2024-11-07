text = input("Введите текст: ")
words = text.split()
every_third_word = words[2::3]
result = " ".join(every_third_word)
print(result)
