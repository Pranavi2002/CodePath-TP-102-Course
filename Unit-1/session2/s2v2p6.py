def reverse_vowels(s):
    # vowels = set('aeiouAEIOU')
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)

s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))