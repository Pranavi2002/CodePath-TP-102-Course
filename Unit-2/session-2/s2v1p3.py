def navigate_research_station(station_layout, observations):
    # Map station characters to their indices
    index_map = {char: idx for idx, char in enumerate(station_layout)}
    
    total_time = 0
    current_index = 0  # Start at index 0 of station_layout (not of observations)

    for ch in observations:
        next_index = index_map[ch]
        total_time += abs(next_index - current_index)
        current_index = next_index

    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  # Output: 45
print(navigate_research_station(station_layout2, observations2))  # Output: 4
