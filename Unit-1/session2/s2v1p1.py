def reverse_sentence(sentence):
    words = sentence.split()
    if len(words) <= 1:
        return sentence
    reversed_words = words[::-1]
    ans = ' '.join(reversed_words)
    return ans

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))