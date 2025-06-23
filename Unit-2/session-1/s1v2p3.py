def check_oxygen_levels(oxygen_levels, min_val, max_val):
    result = []
    for room, level in oxygen_levels.items():
        if level < min_val or level > max_val:
            result.append(room)
    return result

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))