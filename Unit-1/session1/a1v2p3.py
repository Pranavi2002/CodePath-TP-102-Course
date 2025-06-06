def shuffle(message, indices):
    n = len(indices)
    res = [''] * n  # Preallocate a list of correct size with empty strings

    for j in range(n):
        res[indices[j]] = message[j]  # Place each character at the correct index

    return ''.join(res)  # Join list into a string



message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))
