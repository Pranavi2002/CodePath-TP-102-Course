def distinct_averages(species_populations):
    temp = set()
    while len(species_populations) > 0:
        min_sp = min(species_populations)
        max_sp = max(species_populations)
        avg = (min_sp + max_sp)/2
        temp.add(avg)
        species_populations.remove(min_sp)
        species_populations.remove(max_sp)
    return len(temp)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 