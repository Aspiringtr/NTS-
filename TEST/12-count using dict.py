name = 'ENGINEERING'
counts = {}
for letter in name:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1
print("Letter Counts:", counts)