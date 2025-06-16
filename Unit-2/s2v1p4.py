def prioritize_observations(observed_species, priority_species):
    temp = [x for x in observed_species if x not in priority_species]
    ans = priority_species.copy()
    ans.extend(temp)
    return ans

    # from collections import Counter
    # count = Counter(observed_species)
    # result = []
    # for species in priority_species:
    #     result.extend([species] * count[species])
    #     del count[species]
    # for species in sorted(count):
    #     result.extend([species * count[species]])   
    # return result

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2))