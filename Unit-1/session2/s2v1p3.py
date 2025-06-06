def delete_minimum_elements(hunny_jar_sizes):

    # hunny_jar_sizes.sort()
    # print(hunny_jar_sizes)

    ans = []
    while len(hunny_jar_sizes):
        i = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(i)
        ans.append(i)
    print(ans)



hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)