password = input("Enter the password: ")

if len(password) < 8:
    print("Need at least 8 characters")
    print("Weak Password")
else:
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

    if not has_letter:
        print("Need at least one letter")
        print("Weak Password")
    elif not has_number:
        print("Need at least one number")
        print("Weak Password")
    else:
        print("Strong Password")
