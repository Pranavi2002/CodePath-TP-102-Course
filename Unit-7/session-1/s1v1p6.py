def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    maxElem = strongest_avenger(strengths[1:])
    if strengths[0] > maxElem:
        return strengths[0]
    else:
        return maxElem

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))