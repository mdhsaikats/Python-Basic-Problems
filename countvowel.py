name = input("Enter the word: ")

print(len(name))

flag = 0

for n in name:
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        flag += 1

print("Vowels:", flag)
