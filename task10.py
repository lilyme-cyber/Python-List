nums = [1,2,3,4,5,6,7,8,9]
index = int(input(f"Index kiriting (0-{len(nums) - 1}): "))

if 0 <= index < len(nums):
    value = int(input("Qiymat kiriting: "))
    nums[index] = value
else:
    print("Siz xato index tanladingiz!")

print(nums)
