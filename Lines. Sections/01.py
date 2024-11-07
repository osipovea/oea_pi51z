words = set()
while True:
    word = input("Введите элемент множества (введите стоп для завершения): ")
    if word == "стоп":
        break
    words.add(word)
shortest_word = min(words, key=len)
longest_word = max(words, key=len)

shortest_word_characters_set = set(shortest_word.lower())
longest_word_characters_set = set(longest_word.lower())
print('ДА' if shortest_word_characters_set.issubset(longest_word_characters_set) else 'НЕТ')
