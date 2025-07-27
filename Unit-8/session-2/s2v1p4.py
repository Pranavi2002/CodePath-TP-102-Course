def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    if name >= collection.val:
        collection.right= add_plant(collection.right, name)
    else:
        collection.left = add_plant(collection.left, name)
    return collection