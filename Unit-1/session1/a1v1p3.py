import re

def tiggerfy(word):
    # Remove substrings: 't', 'i', 'gg', 'er', case insensitive
    # Note: order matters, so 'gg' and 'er' are matched before single letters to avoid partial matches.
    pattern = r'(?i)gg|er|t|i'
    cleaned = re.sub(pattern, '', word)
    return '"' + cleaned + '"'

# Test cases
print(tiggerfy("suspicerous"))  # removes 'i', 'er' → "supscous"
print(tiggerfy("Trigger"))      # removes 't', 'i', 'gg', 'er' → ""
print(tiggerfy("Hunny"))        # removes 'i' (none), 't'(none), 'gg'(none), 'er'(none) → "Hunny"