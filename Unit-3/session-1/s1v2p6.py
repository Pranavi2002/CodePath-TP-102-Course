from collections import deque
def apply_rating_operations(ratings):
    # # without stack:
    # for i in range(len(ratings)-1):
    #     if ratings[i] == ratings[i+1]:
    #         ratings[i] *= 2
    #         ratings[i+1] = 0
    
    # way-1 using different lists
    # zeroes = ratings.count(0)
    # non_zeroes = [num for num in ratings if num != 0]
    # result = non_zeroes + [0] * zeroes
    # return result

    # # way-2 using the same ratings list
    # #  Shift non-zeroes to the front
    # insert_pos = 0
    # for i in range(len(ratings)):
    #     if ratings[i] != 0:
    #         ratings[insert_pos] = ratings[i]
    #         insert_pos += 1

    # # Fill the rest with zeroes
    # while insert_pos < len(ratings):
    #     ratings[insert_pos] = 0
    #     insert_pos += 1

    # return ratings

    # #with stack:
    # stack = []
    # i = 0
    # while i < len(ratings):
    #     if i < len(ratings) - 1 and ratings[i] == ratings[i + 1]:
    #         stack.append(ratings[i] * 2)
    #         stack.append(0)  # Marking the next one as 0 like in original logic
    #         i += 2  # Skip the next one since it's merged
    #     else:
    #         stack.append(ratings[i])
    #         i += 1

    # # Now shift all zeroes to the end
    # non_zeroes = [x for x in stack if x != 0]
    # zeroes = stack.count(0)
    # return non_zeroes + [0] * zeroes

    # with queue:
    q = deque()
    i = 0

    # Step 1: Merge adjacent duplicates
    while i < len(ratings):
        if i < len(ratings) - 1 and ratings[i] == ratings[i + 1]:
            q.append(ratings[i] * 2)
            q.append(0)  # Insert 0 to simulate second element being wiped
            i += 2
        else:
            q.append(ratings[i])
            i += 1

    # Step 2: Shift all zeroes to end
    non_zeroes = [x for x in q if x != 0]
    zeroes = q.count(0)
    return non_zeroes + [0] * zeroes

print(apply_rating_operations([1, 2, 2, 1, 1, 0])) 
print(apply_rating_operations([0, 1])) 