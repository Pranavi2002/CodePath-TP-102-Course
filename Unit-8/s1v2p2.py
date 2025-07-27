class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def mertwins(root):
    if not root:
        return False
    left = root.left
    right = root.right
    if left and right and left.val == right.val:
        return True
    else:
        return False

"""
      Mermother
       /    \
    Coral   Coral
"""
root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))

"""
      Merpapa
       /    \
   Calypso  Coral
"""
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))

"""
      Merenby
           \    
         Calypso  
"""
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3))