def non_decreasing(nums):
    count = 0
    i = 1
    for i in range(len(nums)):
        if nums[i-1] > nums[i]:
            count += 1
    if count == 1:
        return True
    return False

nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))