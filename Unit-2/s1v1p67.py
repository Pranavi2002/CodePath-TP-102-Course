# without dictionary
def max_audience_performances(audiences):
    max_value = max(audiences)
    count = audiences.count(max_value)
    return max_value * count

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

# with dictionary
def max_audience_performances(audiences):
    freq_map = {}
    
    for audience in audiences:
        if audience in freq_map:
            freq_map[audience] += 1
        else:
            freq_map[audience] = 1
    
    max_value = max(freq_map.keys())
    return max_value * freq_map[max_value]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1)) 
print(max_audience_performances(audiences2)) 