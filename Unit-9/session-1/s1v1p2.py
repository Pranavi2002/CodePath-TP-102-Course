from collections import deque


class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    # base case
    if not design:
        return []
    
    result = []
    queue = deque([design])
    
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(print_design(croquembouche))