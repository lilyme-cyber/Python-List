nums = []
for i in range(10):
    num = int(input(f"{i+1}-sonni kiriting: "))
    nums.append(num)

unique_num = []
for son in nums:
    if nums.count(son) == 1:
        unique_num.append(son)

print(unique_num)
