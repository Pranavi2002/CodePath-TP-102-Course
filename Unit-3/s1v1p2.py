def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)
    reversed_comments = []
    while stack:
        c = stack.pop()
        reversed_comments.append(c)
    return reversed_comments

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))