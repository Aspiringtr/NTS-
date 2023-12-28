import os
source1 = "E:/pythoncode/python/TEST/21-copying from two source to one/aa.txt"
source2 = "E:/pythoncode/python/TEST/21-copying from two source to one/b.txt"
target = "E:/pythoncode/python/TEST/21-copying from two source to one/target.txt"
if os.path.exists(source1):
    with open(source1, 'r') as source_file:
        content = source_file.read()
    with open(target, 'w') as target_file:
        target_file.write(content)
    print("Content from source1 copied to target")
else:
    print("source1 not found")
if os.path.exists(source2):
    with open(source2, 'r') as source_file:
        content = source_file.read()
    with open(target, 'a') as target_file:
        target_file.write(content)
    print("Content from source2 copied to target")
else:
    print("source2 not found")