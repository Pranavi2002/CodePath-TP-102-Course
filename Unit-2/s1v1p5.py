def best_set(votes):
    freq_map = {}
    for value in votes.values():
        if value in freq_map:
            freq_map[value] += 1
        else:
            freq_map[value] = 1
    
    max_votes = 0
    winner = ''
    for artist in freq_map:
        if freq_map[artist] > max_votes:
            max_votes = freq_map[artist]
            winner = artist

    return winner

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))