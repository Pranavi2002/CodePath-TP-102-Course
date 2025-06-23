def max_number_of_string_pairs(signals):
    rev = ''
    count = 0
    for i in range(len(signals) - 1):
        rev = signals[i][::-1]
        for j in range(i+1, len(signals)):
            if signals[j] == rev:
                count += 1
    return count

signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))