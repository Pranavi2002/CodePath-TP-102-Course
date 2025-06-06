def shuffle(message, indices):
    n = len(indices)
    res = [0] * n
    j = 0
    for i in indices:
        res.insert(i, message[j])
        j += 1

    ans = ''
    for string in res:
        ans = res+string
    
    return ans



message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)
