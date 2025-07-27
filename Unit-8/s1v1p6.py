class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Recursive approach:
def survey_tree(root):
    if not root:
        return []
    result = []
    # result += survey_tree(root.left)
    # result += survey_tree(root.right)
    result.extend(survey_tree(root.left))
    result.extend(survey_tree(root.right))
    result.append(root.val)
    return result

# # Iterative approach - 1:
# def survey_tree(root):
#     if not root:
#         return []
    
#     stack, result = [root], []
#     visited = set() # to mark nodes whose children have been pushed
    
#     while stack:
#         node = stack[-1]
#         # If node is a leaf or children already visited
#         if (not node.left and not node.right) or node in visited:
#             result.append(node.val)
#             stack.pop()
#         else:
#             # Push right and left children if they exist
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#             visited.add(node)
#     return result

# # Iterative approach-2 -> two stack approach:
# def survey_tree(root):
#     if not root:
#         return []

#     stack1 = [root]
#     stack2 = []
#     result = []

#     while stack1:
#         node = stack1.pop()
#         stack2.append(node)
#         if node.left:
#             stack1.append(node.left)
#         if node.right:
#             stack1.append(node.right)

#     while stack2:
#         node = stack2.pop()
#         result.append(node.val)

#     return result

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))