class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    left = root.left
    right = root.right
    # if root.val == "+":
    #     return left.val + right.val
    # elif root.val == "-":
    #     return left.val - right.val
    # elif root.val == "*":
    #     return left.val * right.val
    # elif root.val == "/":
    #     return left.val / right.val
    return eval(str(left.val) + root.val + str(right.val))

"""
    +
  /   \
 7     5
"""
apple_tree1 = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree1))

"""
    -
  /   \
 7     5
"""
apple_tree2 = TreeNode("-", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree2))

"""
    *
  /   \
 7     5
"""
apple_tree3 = TreeNode("*", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree3))

"""
    /
  /   \
 7     5
"""
apple_tree4 = TreeNode("/", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree4))
