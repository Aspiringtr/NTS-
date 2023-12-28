my_list = list(map(int, input("Enter the elements separated by space: ").split()))
position_to_insert = int(input("Enter the position to insert: "))
element_to_insert = int(input("Enter the element to insert: "))
my_list.insert(position_to_insert, element_to_insert)
print("List after inserting element:", my_list)
element_to_remove = int(input("Enter the element to remove: "))
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print("List after removing element:", my_list)
else:
    print(f"Element {element_to_remove} not found in the list.")
element_to_find = int(input("Enter the element to find: "))
if element_to_find in my_list:
    position = my_list.index(element_to_find)
    print(f"Position of element {element_to_find}: {position}")
else:
    print(f"Element {element_to_find} not found in the list.")
my_list.clear()
print("List after deleting the entire list:", my_list)