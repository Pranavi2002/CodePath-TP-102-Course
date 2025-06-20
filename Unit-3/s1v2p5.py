def min_remaining_watchlist(watchlist):
    stack = []
    for char in watchlist:
        if not stack:
            stack.append(char)
        else:
            c = stack[-1]
            s = c + char
            if s == 'AB' or s == 'CD':
                stack.pop()
            else:
                stack.append(char)
    return len(stack)

print(min_remaining_watchlist("ABFCACDB")) 
print(min_remaining_watchlist("ACBBD")) 