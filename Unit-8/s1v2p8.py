class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def ocean_depth(root):
    if not root:
        return 0
    return 1 + max(ocean_depth(root.left), ocean_depth(root.right))


"""
                Sunlight
               /        \
              /          \
          Twilight      Squid
         /       \           \   
      Abyss  Anglerfish    Giant Squid
      /
  Trenches
"""
ocean = TreeNode("Sunlight", 
                TreeNode("Twilight", 
                        TreeNode("Abyss", 
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))

"""
    Spray Zone
    /         \
   /           \ 
Beach       High Tide
            /  
      Middle Tide
              \
            Low Tide
"""
tidal_zones = TreeNode("Spray Zone", 
                      TreeNode("Beach"), 
                              TreeNode("High Tide", 
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))