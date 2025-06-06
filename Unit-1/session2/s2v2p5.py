def move_zeroes(lst):
    ans = []
    count = 0
    for num in lst:
        if num == 0:
            count += 1
        else:
            ans.append(num)
    while count > 0:
        ans.append(0)
        count -= 1
    print(ans)

lst = [1, 0, 2, 0, 3, 0]
move_zeroes(lst)