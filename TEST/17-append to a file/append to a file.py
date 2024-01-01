text_to_append = input("Enter the text to append: ")
file_name = "text_file.txt"
with open(file_name, "a") as file:
    file.write(text_to_append + "\n")
with open(file_name, "r") as file:
    file_content = file.read()
print("Text appended to the file:")
print(file_content)
