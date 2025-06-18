words = []
big_words = []

for i in range(1, 6):
    word = input(f"{i} - so'zni kiriting: ").strip()
    words.append(word)

for word in words:
    if len(word) > 5:
        big_words.append(word)

print(big_words)
