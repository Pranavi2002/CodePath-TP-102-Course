def make_divisible_by_3(nums):
    c = 0
    for num in nums:
        if num % 3 != 0:
            c += 1
    print(c)

nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)