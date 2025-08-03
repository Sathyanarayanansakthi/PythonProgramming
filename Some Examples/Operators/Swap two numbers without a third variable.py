# Swap two numbers without a third variable

num1=int(input("Enter First Number : "))
num2=int(input("Enter second Number : "))

num1=num1+num2
num2=num2+num1
num1=num1-num2

print("After swap: num1 =", num1, "num2 =", num2)