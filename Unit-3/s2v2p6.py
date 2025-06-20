def count_balanced_terrain_subsections(terrain):
    groups = []
    count = 1

    # Step 1: Count lengths of consecutive same characters
    for i in range(1, len(terrain)):
        if terrain[i] == terrain[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)  # for the last group

    # Step 2: Count balanced pairs between adjacent groups
    balanced_count = 0
    for i in range(1, len(groups)):
        balanced_count += min(groups[i - 1], groups[i])

    return balanced_count

print(count_balanced_terrain_subsections("00110011")) 
print(count_balanced_terrain_subsections("10101"))