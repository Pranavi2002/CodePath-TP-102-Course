from collections import deque


class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def max_tiers(cake):

    # # DFS:
    # # in order traversal - left, root, right
    # if not cake:
    #     return 0
    # return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

    #BFS:
    if not cake:
        return 0
    height = 0
    queue = deque([cake])
    visited = []
    while queue:
        for _ in range(len(queue)):
        # Loop over the number of elements currently in queue, but I don’t care about the loop variable itself
        # This is often used in Breadth-First Search (BFS) to process all nodes at the current level
            current = queue.popleft()       # queue = []    # queue =['Strawberry'] queue = [] 
            visited.append(current.val)     # visited = ['Chocolate']  visited =['Choco','Van', 'Straw]
            if current.left:
                queue.append(current.left)  # queue = ['Vanilla'] ['Chioco']
            if current.right:
                queue.append(current.right) # queue = ['Vanilla','Strawberry']  ['choco', 'coffe']
        height += 1     # 1 2 3
    return height

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))