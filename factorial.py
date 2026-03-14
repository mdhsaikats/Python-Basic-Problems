num = int(input("Enter the number: "))

factorial = 1


for n in range(1, num + 1):
    factorial = factorial * n

print("Factorial: ", factorial)
