a=int(input("Enter a : "))
b=int(input("Enter b :"))
c=int(input("Enter c :"))

if a>=b and a>=c:
    print("The Largest Number is : ",a)
elif b>=a and b>=c:
    print("The Largest number is : ",b)
elif c>=a and c>=b:
    print("The Largest number is : ",c)
else:
    print(("None"))