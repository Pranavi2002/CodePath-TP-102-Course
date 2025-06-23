def is_symmetrical_title(title):
    title = title.lower()
    title = title.replace(" ", "")
    # return title
    low, high = 0, len(title) - 1
    while low < high:
        if title[low] != title[high]:
            return False
        low += 1
        high -= 1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 