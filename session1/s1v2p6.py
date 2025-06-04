def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]
    return numbers

numbers = [1, 2, 3]
print(squared(numbers))