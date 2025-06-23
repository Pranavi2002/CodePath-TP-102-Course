def make_smallest_watchlist(watchlist):
    shows = list(watchlist)
    left = 0
    right = len(shows) - 1
    while left < right:
        if shows[left] != shows[right]:
            c = shows[left] if shows[left] < shows[right] else shows[right]
            shows[left] = shows[right] = c
        left += 1
        right -= 1
    return ''.join(shows)

print(make_smallest_watchlist("egcfe")) 
print(make_smallest_watchlist("abcd")) 
print(make_smallest_watchlist("seven"))