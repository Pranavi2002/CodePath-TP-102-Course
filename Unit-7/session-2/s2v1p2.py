def find_cabin_index(cabins, preferred_deck):
    def helper_fun(low, high):
        if low > high:
            return low
        mid = (low + high) // 2
        if cabins[mid] > preferred_deck:
            high = mid - 1
            return helper_fun(low, high)
        elif cabins[mid] < preferred_deck:
            low = mid + 1
            return helper_fun(low, high)
        else:
            return mid
    return helper_fun(0, len(cabins) - 1)

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))