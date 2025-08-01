# Take two numbers and print which one is greater.

num1=int(input("Enter the First Number :"))
num2=int(input("Enter the Second Number :"))
if num1 > num2 :
    print(f"{num1} is greater than {num2}.")
elif num2 > num1 :
    print(f"{num2} is greater than {num1}.")
else:
    print("both are equal")