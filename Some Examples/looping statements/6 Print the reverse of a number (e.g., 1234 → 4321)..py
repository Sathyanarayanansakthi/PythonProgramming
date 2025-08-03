# Print the reverse of a number (e.g., 1234 → 4321).
num=int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse =reverse * 10 + digit
    num = num //10
print(reverse)