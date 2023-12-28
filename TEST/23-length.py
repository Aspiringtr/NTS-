def reverse(name):
    if len(name) % 3 == 0:
        reversed_str = name[::-1]
        print("Reversed String:", reversed_str)
    else:
        print("String remains unchanged:", name)
name = input("Enter a string: ")
reverse(name)