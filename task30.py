words = []
for _ in range(5):
    word = input("soz kiriting: ")
    words.append(word)

palindrom_words = []
for word in words:
    if word == word[::-1]:
        palindrom_words.append(word)

print(palindrom_words)
