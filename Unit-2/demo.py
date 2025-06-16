# def best_set(votes):
#     freq_map = {}
#     for value in votes.values():
#         if value in freq_map:
#             freq_map[value] += 1
#         else:
#             freq_map[value] = 1
#     maxVotes = 0
#     artist = ''
#     for key, val in freq_map.items():
#         if val > maxVotes:
#             maxVotes = val
#             artist = key
#     return artist


# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))

def max_audience_performances(audiences):
    freq_map = {}
    for size in audiences:
        if size in freq_map:
            freq_map[size] += 1
        else:
            freq_map[size] = 1
    maxSize = 0
    result = 0
    for key, val in freq_map.items():
        if key > maxSize:
            maxSize = key
            result = maxSize * val
    return result

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))