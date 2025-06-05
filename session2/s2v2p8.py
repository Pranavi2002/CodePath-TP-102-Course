def left_right_difference(nums):
    n = len(nums)
    ans = [0] * n # declare an array of size n and initlialize with zeroes

    left = 0
    for i in range(n):
        ans[i] = left
        left += nums[i]

    right = 0
    for j in range(n-1, -1, -1):
        ans[j] -= right
        right += nums[j]

    return ans

nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))