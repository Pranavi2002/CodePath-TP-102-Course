def find_difference(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)
    list1 = list(set1 - set2)
    list2 = list(set2 - set1)
    # ans = list1 + list2 
    ans = []
    ans.append(list1)
    ans.append(list2)
    return ans

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))