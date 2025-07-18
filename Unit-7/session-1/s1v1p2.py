def sum_stones(stones):
    if not stones:
        return 0 
    else:
        return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))