num = int(input("Enter the number: "))
if num <= 1:
    print("Not Prime")
else:
    for n in range(2, num):
        if num % n == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
