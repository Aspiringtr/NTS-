def largest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    third_largest = sorted_numbers[2]
    return third_largest
input_list = list(map(int, input("Enter the elements separated by space: ").split()))
print(input_list)
result = largest(input_list)
print(f"The third largest number in the list is: {result}")