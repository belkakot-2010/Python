'''Задача 3'''

nums = input('Введите элементы списка через пробел: ').split
for i in range(len(nums)):
    nums[i] = int(nums[i])


def Buble_cort(nums: list) -> None:
    col = 0
    for num_index in range(len(nums) - 1):
        for i in range(num_index, len(nums) - 1):
            col += 1
            if nums[i] > nums[i+1]:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

    return col    


print(nums)
Buble_cort(nums)
col = Buble_cort(nums)
print(col)