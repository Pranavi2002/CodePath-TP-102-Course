def concatenate(words):
        return '"' + ''.join(words) + '"'

words = ["vengeance", "darkness", "batman"]
print(concatenate(words))

words = []
print(concatenate(words))