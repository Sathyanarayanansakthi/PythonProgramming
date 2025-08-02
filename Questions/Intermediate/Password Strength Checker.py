password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short")
elif not any(char.isalpha() for char in password):
    print("Password must contain at least one letter")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one number")
else:
    print("Password is strong")
