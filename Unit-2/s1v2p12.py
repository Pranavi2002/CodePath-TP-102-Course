def find_final_hub(paths):
    if len(paths) == 1:
        return paths[0][1]
    start = []
    dest = []
    for i in range(len(paths)):
        start.append(paths[i][0])
        dest.append(paths[i][1])
    # final_dest is a generator object, so use next() to get the first item
    final_dest = next(x for x in dest if x not in start)
    return final_dest 

paths1 = [["Earth", "Mars"], ["Titan", "Europa"], ["Mars", "Titan"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))
