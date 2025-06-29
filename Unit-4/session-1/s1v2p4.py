#Method-1:
def reverse_memes(memes):
    memes.reverse() # modifies the original list, in-place
    return memes

memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))
# O(n) TC, O(1) SC

#Method-2:
def reverse_memes(memes):
    return memes[::-1]  # slicing creates a reversed copy
# O(n) TC, O(n) SC

#Method-3:
def reverse_memes(memes):
    return list(reversed(memes))  # also returns a reversed copy
# O(n) TC, O(n) SC