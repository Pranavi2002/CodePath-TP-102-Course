# # without inner function
# def post_compare(draft1, draft2):
#     stack1 = []
#     stack2 = []
#     for c in draft1:
#         if c != '#':
#             stack1.append(c)
#         elif stack1:
#             stack1.pop()
#     for c in draft2:
#         if c != '#':
#             stack2.append(c)
#         elif stack2:
#             stack2.pop()
        
#     # if ''.join(stack1) == ''.join(stack2):
#     if stack1 == stack2:
#         return True
#     else:
#         return False

# print(post_compare("ab#c", "ad#c"))
# print(post_compare("ab##", "c#d#")) 
# print(post_compare("a#c", "b")) 

# with inner function:
def post_compare(draft1, draft2):
    def build_draft(draft):
        stack = []
        for c in draft:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    
    return build_draft(draft1) == build_draft(draft2)

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 