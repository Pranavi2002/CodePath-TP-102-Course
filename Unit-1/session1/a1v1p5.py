def find_missing_clues(clues, lower, upper):
   cluesList = []
   
   if clues[0] > lower:
       cluesList.append([lower, clues[0] - 1])
   for i in range(len(clues) - 1):
        if clues[i+1] - clues[i] > 1:
            cluesList.append([clues[i] + 1, clues[i + 1] - 1])
            
   if clues[len(clues) - 1] < upper:
       cluesList.append([clues[len(clues) - 1] + 1, upper])
   return cluesList


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))
clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))