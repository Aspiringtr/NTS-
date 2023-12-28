import os
file_path = "E:/pythoncode/python/TEST/24-no of words present in a file/aa.txt"
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        num_words = len(words)
        print(f"The number of words in the file is: {num_words}")
else:
    print("File not found")