def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    total_difference = 0

    for  c in s:
        difference = abs(s.index(c) - t.index(c))
        total_difference += difference

    return total_difference

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))