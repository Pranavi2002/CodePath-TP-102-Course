def collect_festival_points(points):
    stack = []
    for point in points:
        stack.append(point)
    count = 0
    while stack:
        count += stack.pop()
    return count

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 