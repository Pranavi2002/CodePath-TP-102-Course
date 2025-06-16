def sort_performers(performer_names, performance_times):
    # Pair each performer with their time
    paired = list(zip(performer_names, performance_times))
    # Sort by the performance time (the second element in the tuple)
    paired_sorted = sorted(paired, key=lambda x: x[1], reverse=True)
    # Extract and return the sorted performer names
    return [name for name, time in paired_sorted]

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))