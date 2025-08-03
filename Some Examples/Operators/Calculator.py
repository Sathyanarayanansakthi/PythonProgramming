num1=float(input("Enter the First Number"))
num2=float(input("Enter the Second Number"))
operators=(input("Enter the Operators (+,-,*,/) :"))

if operators == "+":
    result =num1+num2
    print("The Result is" , result)
elif operators == "-":
    result =num1-num2
    print("The Result is ", result)
elif operators == "*":
    result =num1*num2
    print("The Result is ", result)
elif operators == "/":
    if num2 !=0:
     result =num1 / num2
    print("The Result is ", result)

else:
    print("Invalid Operator")