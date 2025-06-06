def can_pair(item_quantities):
    items = len(item_quantities)
    count = 0
    for i in item_quantities:
        if i%2 == 0:
            count += 1
    if count == items:
        return True
    else:
        return False

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))