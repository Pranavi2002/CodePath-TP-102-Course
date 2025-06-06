def split_haycorns(quantity):
    ans = []
    if quantity == 1:
        ans.append(quantity)
    else:
        i = 1
        while i <= quantity/2:
            if quantity % i == 0:
                ans.append(i)
            i += 1
        ans.append(quantity)
    print(ans)

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)