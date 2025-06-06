def goldilocks_approved(nums):
    a = min(nums)
    b = max(nums)
    res = -1
    for i in nums:
        if i > a and i < b:
            res = i 
    return res

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
