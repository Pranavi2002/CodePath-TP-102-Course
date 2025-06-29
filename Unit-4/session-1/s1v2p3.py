# Method-1:
from collections import Counter
def find_trending_memes(memes):
    counter = Counter(memes)
    return [item for item, freq in counter.items() if freq > 1]

memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))
# O(n) TC, O(n) SC

# Method-2:
def find_trending_memes(memes):
    seen = set()
    duplicates = set()
    for item in memes:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
# O(n) TC, O(n) SC
