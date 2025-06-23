# def schedule_pattern(pattern, schedule):
    
#     genres = schedule.split()

#     if len(genres) != len(pattern):
#         return False

#     char_to_genre = {}
#     genre_to_char = {}

#     for char, genre in zip(pattern, genres):
#         if char in char_to_genre:
#             if char_to_genre[char] != genre:
#                 return False
#         else:
#             char_to_genre[char] = genre

#         if genre in genre_to_char:
#             if genre_to_char[genre] != char:
#                 return False
#         else:
#             genre_to_char[genre] = char

#     return True

# pattern1 = "abba"
# schedule1 = "rock jazz jazz rock"

# pattern2 = "abba"
# schedule2 = "rock jazz jazz blues"

# pattern3 = "aaaa"
# schedule3 = "rock jazz jazz rock"

# print(schedule_pattern(pattern1, schedule1))
# print(schedule_pattern(pattern2, schedule2))
# print(schedule_pattern(pattern3, schedule3))

def schedule_pattern(pattern, schedule):
    words = schedule.split()
    if len(words) != len(pattern):
        return False

    def get_pattern_ids(seq):
        mapping = {}
        result = []
        next_id = 0
        for x in seq:
            if x not in mapping:
                mapping[x] = next_id
                next_id += 1
            result.append(mapping[x])
        return result

    return get_pattern_ids(pattern) == get_pattern_ids(words)

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))
