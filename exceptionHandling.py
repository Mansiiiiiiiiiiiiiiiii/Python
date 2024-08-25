a=input("Enter the number")
print("Multiplication table of {a} is:")
try:
    for i in range(10):
        print(f"{int (a)} x {i} ={int(a)*i}")
except:
    print("Invalid Input!")

print("Some imp line of code")
print("End of program")

try:
    num=int(input("Enter an integer"))
except ValueError:
    print("Number is not an integer")

#-----------------------------------------------Many Exceptions------------------------------------------------------------------------------

x = input("Enter your name")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#-----------------------------------------------Else-------------------------------------------------------------------------------------------

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#----------------------------------------------Finally-----------------------------------------------------------------------------------------

def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index"))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")
x=func1()
print(x)

#useful to close objects and clean up resources

try:
    # Open the file in write mode
    f = open("demofile.txt", "w")
    try:
        f.write("Hello !! Mansi is here")
    except:
        print("Something went wrong while writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong in opening the file")

#--------------------------------------------------------------Raise an exception---------------------------------------------------------------

x=-1
if x<0:
    raise Exception("No member below zero")

x="Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")