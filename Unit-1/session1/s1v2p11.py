def running_sum(superhero_stats):
    for i in range(1,len(superhero_stats)):
        superhero_stats[i] += superhero_stats[i-1]
    print(superhero_stats)

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)