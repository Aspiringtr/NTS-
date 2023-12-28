input_sequence = input("Enter a comma-separated sequence of words: ").split(',')
unique_sorted_words = sorted(set(input_sequence))
print("Unique words in sorted form:",unique_sorted_words)