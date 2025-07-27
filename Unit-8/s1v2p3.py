class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    if not root:
        return False

    # Base case: if it's a leaf node
    if not root.left and not root.right:
        return root.val

    # Recursively evaluate left and right children
    left_val = get_decision(root.left)
    right_val = get_decision(root.right)
    
    # Apply boolean operation
    if root.val == 'AND':
        return left_val and right_val
    elif root.val == 'OR':
        return left_val or right_val
    else:
        raise ValueError(f"Invalid operation: {root.val}")

"""
        OR
      /    \
    True  False
"""
expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

"""
       False
"""
expression2 = TreeNode(False)

print(get_decision(expression1))
print(get_decision(expression2))