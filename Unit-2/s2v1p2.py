def count_endangered_species(endangered_species, observed_species):
    # end_set = list(endangered_species)
    count = 0
    for sp in observed_species:
        if sp in endangered_species:
            count += 1
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 