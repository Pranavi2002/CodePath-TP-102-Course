class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Recursive approach:
def right_vine(root):
    result = []
    if root is None:
        return result
    result.append(root.val)
    # adds the current node’s value
    result.extend(right_vine(root.right)) 
    # recursively gathers values from the right subtree and adds them to the same list
    return result

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))