n1 = int(input("Enter any number"))
n2 = int(input("Enter other number"))
s = input("Enter the arithmetic operator")
if s == '+':
    print(n1+n2)
elif s == '-':
    print(n1-n2)
elif s == '*':
    print(n1*n2)
elif s=='/':
    print(n1/n2)
elif s=='%':
    print(n1%n2)
elif s=='**':
    print(n1**n2)
elif s=='//':
    print(n1//n2)
else:
    print("Not an Arithmetic Operator")
