# Plain Version:
def fibonacci_growth(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_growth(n-2) + fibonacci_growth(n-1)

print(fibonacci_growth(5))
print(fibonacci_growth(8))
# Exponential time complexity

# Memoized Version:
def fibonacci_cache_growth(n, cache = {}):
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        res = fibonacci_cache_growth(n-2, cache) + fibonacci_cache_growth(n-1, cache)
        cache[n] = res
    return cache[n]

print(fibonacci_cache_growth(5))
print(fibonacci_cache_growth(8))
# Linear Time Complexity, avoids redundant calls 