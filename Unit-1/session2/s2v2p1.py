def are_equivalent(word1, word2):
    c1 = ''.join(word for word in word1)
    c2 = ''.join(word for word in word2)
    return c1 == c2

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))