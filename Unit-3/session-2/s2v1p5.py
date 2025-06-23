def merge_schedules(schedule1, schedule2):
    stack = []
    p1, p2 = 0, 0
    len1, len2 = len(schedule1), len(schedule2)
    
    # Alternate adding characters
    while p1 < len1 and p2 < len2:
        stack.append(schedule1[p1])
        p1 += 1
        stack.append(schedule2[p2])
        p2 += 1
    
    # Append remaining from schedule1
    while p1 < len1:
        stack.append(schedule1[p1])
        p1 += 1

    # Append remaining from schedule2
    while p2 < len2:
        
        stack.append(schedule2[p2])
        p2 += 1
    
    return ''.join(stack)

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 