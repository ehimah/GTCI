"""
[3, 1, 5, 4, 2]

i = 0
3 != 2
[5, 1, 3, 4, 2]

5!=4
[2, 1, 3, 4, 5]

2 != 1
[1, 2, 3, 4, 5]

[1, 2, 3, 4, 5]
"""


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))
