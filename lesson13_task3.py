def choose_func(nums: list, func1, func2):
        x = 0
        for num in nums:
            if num > 0:
                x = 1
            else:
                x = 0
        func1 = square_nums(nums)
        func2 = remove_negatives(nums)

        if x > 1:
            return func1
        else:
            return func2


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

print(choose_func(nums1, square_nums, remove_negatives))
