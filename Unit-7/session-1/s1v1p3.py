def count_suits_iterative(suits):
    suits_set = set()
    for suit in suits:
        suits_set.add(suit)
    return len(suits_set)

def count_suits_recursive_I(suits):
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        return count_suits_recursive_I(suits[1:])
    else:
        return 1 + count_suits_recursive_I(suits[1:])

def count_suits_recursive_II(suits, seen=None):
    if seen is None:
        seen = set()
    if not suits:
        return len(seen)
    seen.add(suits[0])
    return count_suits_recursive_II(suits[1:], seen)

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive_I(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive_II(["Mark I", "Mark I", "Mark III"]))