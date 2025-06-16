def num_popular_pairs(popularity_scores):
    freq_map = {}
    for score in popularity_scores:
        if score in freq_map:
            freq_map[score] += 1
        else:
            freq_map[score] = 1
    
    pairs = 0
    sum = 0
    for value in freq_map:
        if freq_map[value] != 1:
            n = freq_map[value]
            sum = (n * (n-1))//2
            pairs += sum
    return pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))

#  [1, 2, 3, 1, 1, 3]

#  1 - 3 times
#  n = 3
#  no of pairs of 1 = 3 * 2 / 2 = 3
# 2 - 1 time
# 3 - 2 times
# no of pairs of 3 = 2 * 1 / 2 = 1
# 3 + 1 = 4 