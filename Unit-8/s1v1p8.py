class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    if not root:
        return False

    # # iterative approach:    
    # stack = [root]
    # while stack:
    #     current = stack.pop()
    #     if current.val == flower:
    #         return True
    #     if current.left:
    #         stack.append(current.left)
    #     if current.right:
    #         stack.append(current.right)
    # return False

    # recursive approach:
    if root.val == flower:
        return True
    return find_flower(root.left, flower) or find_flower(root.right, flower)
"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))