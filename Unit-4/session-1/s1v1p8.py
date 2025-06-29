def find_closest_nft_values(nft_values, budget):
    smaller = float('-inf') #O(1) SC
    greater = float('inf')  #O(1) SC
    for nft in nft_values:  #O(n) TC
        if nft < budget and nft > smaller:
            smaller = nft   #O(1) SC
        if nft > budget and nft < greater:
            greater = nft   #O(1) SC
    return (smaller, greater)   # O(n) TC, O(1) SC

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))