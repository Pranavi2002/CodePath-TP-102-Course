def merge_alternately(word1, word2):
    merged = []
    len1, len2 = len(word1), len(word2)
    for i in range(max(len1, len2)):
        if i < len1:
            merged.append(word1[i])
        if i < len2:
            merged.append(word2[i])
    return ''.join(merged)

word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))