list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
result = []

for item in list1:
    if item in list2 and item not in result:
        result.append(item)

print(result)