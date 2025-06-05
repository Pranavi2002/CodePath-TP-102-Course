def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        n = n//10
        count += 1
    return count

n = 964
print(count_digits(n))

n = 0
print(count_digits(n))