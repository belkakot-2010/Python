nums = [23, 23, 6, 17, 43, 0, 23, 67, 782, 34]
j = nums[0]

n = len(nums)
col = 0
for i in range(n):
    for j in range(0, n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            col += 1

print(nums)
print(col)