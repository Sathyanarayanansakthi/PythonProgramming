# Given two numbers, print the smallest using condition
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1 < num2:
    print(f"{num1} is the less that {num2}")
elif num2 < num1:
    print(f"{num2} is the less that {num1}")
else:
    print("both number are equal")