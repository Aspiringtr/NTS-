input_tuple = tuple(map(int, input("Enter the elements separated by space:").split()))
unique_elements = set(input_tuple)
convert_tuple = tuple(unique_elements)
print("Tuple after removing duplicates:", convert_tuple)