import random as rn

num = int(input("Enter your number 1 - 100: "))

if num == rn.randint(1, 100):
    print("Won!")
else:
    print("Lose!")
