import os
file_path = "aa.txt"
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        num_words = len(words)
        print(f"The number of words in the file is: {num_words}")
else:
    print("File not found")
