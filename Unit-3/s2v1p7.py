def sort_performances_by_type(performances):
    if len(performances) <= 1:
        return performances
    evens = []
    odds = []
    for p in performances:
        if p % 2 == 0:
            evens.append(p)
        else:
            odds.append(p)
    result = [evens + odds]
    return result

print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  