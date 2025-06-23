def is_valid_post_format(posts):
    stack = []
    tag_map = {')': '(', ']': '[', '}': '{'}

    for char in posts:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != tag_map.get(char):
                return False
            stack.pop()
    
    return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))