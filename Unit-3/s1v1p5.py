def clean_post(post):
    if len(post) == 1:
        return post
    stack = []
    i = 0
    while i < len(post):
        # if i == 0: 
        #     stack.append(post[i])
        c = post[i]
        if stack:
            # s = stack.peek()
            s = stack[-1]
            # if s.upper() == c or s.lower() == c:
            if s != c and s.lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
        i += 1
    return ''.join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 