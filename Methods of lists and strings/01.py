words = input("Введите любые слова: ").split()
longest_word_length = max(len(word) for word in words)
print(longest_word_length)
