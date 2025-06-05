def expose_superman(trust, n):
    trust_count = [0] * (n + 1)       # How many people each person trusts
    trusted_by_count = [0] * (n + 1)  # How many people trust each person

    for a, b in trust:
        trust_count[a] += 1
        trusted_by_count[b] += 1

    for i in range(1, n + 1):
        if trust_count[i] == 0 and trusted_by_count[i] == n - 1:
            return i  # Superman found

    return -1  # No such person

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))