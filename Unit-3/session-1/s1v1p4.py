def engagement_boost(engagements):
    # # without two pointers:
    # squared_engagements = []
    
    # for i in range(len(engagements)):
    #     squared_engagement = engagements[i] * engagements[i]
    #     squared_engagements.append((squared_engagement, i))
    
    # squared_engagements.sort(reverse=True)
    
    # result = [0] * len(engagements)
    # position = len(engagements) - 1
    
    # for square, original_index in squared_engagements:
    #     result[position] = square
    #     position -= 1
    
    # return result

    # with two pointers:
    #way-1:
    n = len(engagements)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1

    while left <= right:
        left_sq = engagements[left] ** 2
        right_sq = engagements[right] ** 2

        if left_sq > right_sq:
            result[position] = left_sq
            left += 1
        else:
            result[position] = right_sq
            right -= 1

        position -= 1

    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

#way-2:
def engagement_boost(engagements):
    
    left_pointer = 0
    right_pointer = len(engagements) - 1
    while left_pointer<=right_pointer:
        if left_pointer==right_pointer:
            engagements[left_pointer] = engagements[left_pointer] * engagements[left_pointer]
        else:
            engagements[left_pointer] = engagements[left_pointer] * engagements[left_pointer]
            engagements[right_pointer] = engagements[right_pointer] * engagements[right_pointer]
        
        left_pointer+=1
        right_pointer-=1

    engagements.sort()
    
    return engagements

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))