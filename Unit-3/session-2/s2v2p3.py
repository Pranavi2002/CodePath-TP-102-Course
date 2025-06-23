def terrain_elevation_match(terrain):
  n = len(terrain)
  low = 0 
  high = n
  result = []
  for t in terrain:
    if t == 'I':
      result.append(low)
      low += 1
    else:
      result.append(high)
      high -= 1
  result.append(high)
  return result

print(terrain_elevation_match("IDID")) 
print(terrain_elevation_match("III")) 
print(terrain_elevation_match("DDI")) 
  