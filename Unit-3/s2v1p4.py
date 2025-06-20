def booth_navigation(clues):
    stack = []
    for clue in clues:
        if clue != "back":
            stack.append(clue)
        elif clue == "back" and len(stack) != 0:
            stack.pop()
    return stack

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 