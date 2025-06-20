from collections import deque
def edit_post(post):
    words = post.split()
    rev_words = []
    for word in words:
        d = deque(word)
        reversed_word = ''

        while d:
            reversed_word += d.pop()

        rev_words.append(reversed_word)
    return ' '.join(rev_words)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 