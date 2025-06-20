def next_greater_event(schedule1, schedule2):
    result = []
    for sc in schedule1:
        found = False
        for i in range(len(schedule2)):
            if schedule2[i] == sc:
                # search right of sc in schedule2
                for j in range(i + 1, len(schedule2)):
                    if schedule2[j] > sc:
                        result.append(schedule2[j])
                        found = True
                        break
                break  # no need to keep scanning schedule2
        if not found:
            result.append(-1)
    return result

print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4])) 