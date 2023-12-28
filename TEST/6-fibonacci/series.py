import fibo
number = int(input("enter the number"))
for i in range(number):
    print(fibo.fibonacci(i), end=" ")