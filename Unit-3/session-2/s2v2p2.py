def first_symmetrical_landmark(landmarks):
    def is_symmetrical(word):
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    for land in landmarks:
        flag = is_symmetrical(land)
        if flag == True:
            return land
    return ""

print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"])) 