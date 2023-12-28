num_fractions = int(input("Enter the number of fractions to calculate: "))
for denominator in range(2, num_fractions + 2):
    fraction = 1 / denominator
print(f"The decimal equivalent of 1/{denominator} is: {fraction}")
