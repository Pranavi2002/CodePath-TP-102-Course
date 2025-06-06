def is_acronym(words, s):
    c = ''.join(word[0] for word in words)
    return c == s

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

words = ["bear", "pooh"]
s = "pb"
print(is_acronym(words, s))