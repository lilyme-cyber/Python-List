words = ["kitob", "dastur", "AI", "hello", "python", "fdsf", "fasafadsfds"]

group_of_words = [
    [],
    [],
    []
]

for word in words:
    if len(word) <= 3:
        group_of_words[0].append(word)
    elif len(word) <= 6:
        group_of_words[1].append(word)
    else:
        group_of_words[2].append(word)

print(group_of_words)