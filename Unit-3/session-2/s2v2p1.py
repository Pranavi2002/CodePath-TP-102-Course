def final_supply_costs(costs):
    final_costs = []
    for i in range(len(costs)):
        c = costs[i]
        for j in range(i+1, len(costs)):
            if c >= costs[j]:
                c -= costs[j]
                break
        final_costs.append(c)
    return final_costs

print(final_supply_costs([8, 4, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6])) 